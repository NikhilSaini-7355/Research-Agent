from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,   # Target size of the chunk (matches your image spec)
            chunk_overlap=200, # 200 character overlap ensures context bleeds between chunks
            length_function=len,
        )

    def chunk_text(self, raw_text: str) -> list[str]:
        """Splits raw HTML/text into manageable pieces for the Vector DB."""
        if not raw_text:
            return []
        return self.splitter.split_text(raw_text)

# Instantiate the helper
text_processor = TextProcessor()