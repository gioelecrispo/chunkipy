from chunkipy import TextChunker
from chunkipy.text_splitters import WordTextSplitter


if __name__ == "__main__":
    word_text_splitter = WordTextSplitter()

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        text_splitters=[word_text_splitter]
    )

    text = "This is a sample text that will be split into chunks based on word boundaries."
    chunks = text_chunker.chunk(text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")