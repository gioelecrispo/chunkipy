from chunkipy import TextChunker
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


if __name__ == "__main__":
    text = "This is a small text -> with custom split strategy."

    class ArrowTextSplitter(BaseTextSplitter):
        def split(self, text):
            return [t for t in text.split("->") if t != '' and t != ' ']

    # Create a TextChunker object with custom text splitter (using WordSizeEstimator by default)
    arrow_text_splitter = ArrowTextSplitter()
    text_chunker = TextChunker(chunk_size=8, tokens=True, text_splitters=[arrow_text_splitter])
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")