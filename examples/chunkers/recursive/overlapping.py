from chunkipy import RecursiveTextChunker


if __name__ == "__main__":
    # Set up test input
    with open("examples/texts/overlapping.txt", "r") as file:
        text = file.read()

    # Generate chunks with overlapping
    text_chunker = RecursiveTextChunker(50, overlap_ratio=0.3)  # using WordSizeEstimator by default
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate (chunks):
        print(f"Chunk {i + 1}: {chunk}")
