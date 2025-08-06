from chunkipy import TextChunker

if __name__ == "__main__":
    # Set up test input
    text = "In this example test, we are evaluating the overlapping functionality. " \
        "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
        "goal is: 1. to ensure that chunks are generated correctly, 2. check the overlapping. For this purpose, we have chosen a " \
        "long text that exceeds 100 tokens. By setting the overlap_percent to 0.3, we expect the " \
        "generated chunks to have an overlap of approximately 30%. This will help us verify the effectiveness " \
        "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
        "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
        "for proper overlap. "

    # Generate chunks with overlapping
    text_chunker = TextChunker(50, tokens=True, overlap_ratio=0.3)  # using WordSizeEstimator by default
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate (chunks):
        print(f"Chunk {i + 1}: {chunk}")
