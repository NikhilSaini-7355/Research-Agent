from backend.database.chroma_service import chroma_service

from Agents.synthesizer_agent import SynthesizerAgent
from Agents.outline_generator import OutlineGenerator
from Agents.writer import WriterAgent
from src.utils.pdf_generator import save_markdown_as_pdf

def get_context(results_dict):

    docs = results_dict.get("documents", [[]])[0]

    context = []

    for doc in docs:
        clean = (
            doc.replace("\r\n", "\n")
               .replace("\\", "")
               .strip()
        )

        context.append(clean)

    return "\n\n".join(context)


topic = "AI in USA"

query = "Benefits AI has given to the US Citizens"


# -----------------------------
# Step 1 : Research Summary
# -----------------------------

synthesizer = SynthesizerAgent()

research_summary = synthesizer.synthesize_research_summary(
    query=query,
    topic=topic
)


# -----------------------------
# Step 2 : Outline
# -----------------------------

outline_generator = OutlineGenerator()

outline = outline_generator.generate_outline(
    research_summary
)


# -----------------------------
# Step 3 : Write Paper
# -----------------------------

writer = WriterAgent()

paper = []


paper.append(f"# {outline.title}\n")


for section in outline.sections:

    retrieval_query = f"{topic} {section}"

    retrieved = chroma_service.retrieve_by_query(
        retrieval_query,
        5
    )

    context = get_context(retrieved)

    section_result = writer.write_section(
        section=section,
        context=context
    )

    paper.append(f"## {section_result.section_title}\n")

    paper.append(section_result.content)

    paper.append("\n")


# -----------------------------
# Final Markdown
# -----------------------------

final_markdown = "\n".join(paper)

save_markdown_as_pdf(
    markdown_text=final_markdown,
    filename="Research_Paper.pdf"
)
