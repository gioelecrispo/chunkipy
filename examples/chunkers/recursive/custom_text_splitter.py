from chunkipy import RecursiveTextChunker
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


if __name__ == "__main__":
    text = "This is a small text -> with custom split strategy."

    class ArrowTextSplitter(BaseTextSplitter):
        def _split(self, text):
            return [t for t in text.split("->") if t != '' and t != ' ']

    # Create a TextChunker object with custom text splitter (using WordSizeEstimator by default)
    arrow_text_splitter = ArrowTextSplitter()
    text_chunker = RecursiveTextChunker(chunk_size=8, text_splitters=[arrow_text_splitter])
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")