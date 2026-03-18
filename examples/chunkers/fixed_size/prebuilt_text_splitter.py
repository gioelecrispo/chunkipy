from chunkipy import FixedSizeTextChunker


if __name__ == "__main__":
    text_chunker = FixedSizeTextChunker(
        chunk_size=200,
        overlap_ratio=0.25
    )

    text = "This is a sample text that will be split into chunks based on word boundaries."
    chunks = text_chunker.chunk(text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")