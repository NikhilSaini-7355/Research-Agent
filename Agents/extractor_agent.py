import os
import json
from firecrawl import Firecrawl
from dotenv import load_dotenv

from src.utils.clean_markdown import clean_markdown

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")


class ContentExtractor:

    def __init__(self):

        self.firecrawl = Firecrawl(
            api_key=FIRECRAWL_API_KEY
        )

        self.MIN_WORDS = 300
        self.MIN_PARAGRAPHS = 1

        os.makedirs(
            "research_docs",
            exist_ok=True
        )

    def extract_content(
        self,
        search_results
    ):

        saved_count = 0
        failed_count = 0

        metadata_records = []

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

                filename = (
                    f"doc_{saved_count+1}.md"
                )

                filepath = os.path.join(
                    "research_docs",
                    filename
                )

                with open(
                    filepath,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(
                        cleaned_content
                    )

                metadata_records.append({

                    "file": filename,

                    "url": url,

                    "title": getattr(
                        result,
                        "title",
                        ""
                    ),

                    "score": getattr(
                        result,
                        "score",
                        None
                    ),

                    "word_count": word_count,

                    "paragraph_count": paragraph_count
                })

                saved_count += 1

                print(
                    f"Saved: {filename}"
                )

            except Exception as e:

                failed_count += 1

                print(
                    f"Failed: {url}"
                )

                print(e)

        # --------------------------
        # Save metadata
        # --------------------------

        with open(
            "research_docs/metadata.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata_records,
                f,
                indent=4
            )

        print("\n" + "=" * 50)

        print(
            f"Saved Documents: {saved_count}"
        )

        print(
            f"Failed Documents: {failed_count}"
        )

        print("=" * 50)