import os
import json
from firecrawl import Firecrawl
from dotenv import load_dotenv
import shutil
from Agents.content_quality_evaluator import (
    ContentQualityEvaluator
)
from src.utils.clean_markdown import clean_markdown
import uuid
from backend.database.database_session import AsyncSessionLocal
from Schemas.all_db_schemas import ExtractedContentCreate
from backend.database.crud_agents import crud_content

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")


class ContentExtractor:

    def __init__(self):

        self.firecrawl = Firecrawl(
            api_key=FIRECRAWL_API_KEY
        )

        self.MIN_WORDS = 300
        self.MIN_PARAGRAPHS = 1

        self.evaluator = ContentQualityEvaluator()

    async def extract_content(
        self,
        search_results,
        project_id
    ):

        success_count = 0
        failed_count = 0
        project_id = uuid.UUID(project_id)

        seen_urls = set()

        for result in search_results:

            try:

                url = str(result.url)

                if url in seen_urls:
                    continue

                seen_urls.add(url)

                print(f"\nScraping: {url}")

                doc = self.firecrawl.scrape(
                    url,
                    only_main_content=True,
                    formats=["markdown"]
                )

                cleaned_content = clean_markdown(
                    doc.markdown
                )

                if not cleaned_content:
                    print("Rejected: Empty after cleaning")
                    continue

                # --------------------------
                # Quality checks
                # --------------------------

                word_count = len(
                    cleaned_content.split()
                )

                paragraphs = [

                    p.strip()

                    for p in cleaned_content.split("\n\n")

                    if len(p.strip()) > 50
                ]

                paragraph_count = len(
                    paragraphs
                )

                if word_count < self.MIN_WORDS:

                    print(
                        f"Rejected: only {word_count} words"
                    )

                    continue

                if paragraph_count < self.MIN_PARAGRAPHS:

                    print(
                        f"Rejected: only {paragraph_count} paragraphs"
                    )

                    continue

                # --------------------------
                # Save markdown
                # --------------------------

                evaluation_result = self.evaluator.evaluate(
                    cleaned_content[:8000]
                )

                quality = evaluation_result.quality.upper()

                if quality == "HIGH":
                    async with AsyncSessionLocal() as session:
                        try:
                            content_data = ExtractedContentCreate(
                                project_id=project_id,
                                url=url,
                                title=getattr(result, "title", "Untitled Document"),
                                raw_content=cleaned_content
                            )

                            await crud_content.create(
                                db=session,
                                obj_in=content_data
                            )
                            print(f"Ready to saved to DB: {url}")
                            await session.commit()
                            success_count += 1
                        except Exception as e:
                            import traceback
                            traceback.print_exc()  # <--- Add this line to bypass CustomException masking
                            print(f"\n❌ Extracted Content Saving Failed: {e}")
                            await session.rollback()
                            raise e

            except Exception as e:

                failed_count += 1

                print(
                    f"Failed: {url}"
                )

                print(e)
        
        print("\n" + "=" * 50)

        print(
            f"Extracted Documents: {success_count}"
        )

        print(
            f"Failed Documents: {failed_count}"
        )

        print("=" * 50)


