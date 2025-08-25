from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator
from chunkipy import RecursiveTextChunker


if __name__ == "__main__":
    
    class HalfLengthSizeEstimator(BaseSizeEstimator):
        def estimate_size(self, text):
            # Implement your custom size estimation logic here
            return int(len(text)/2)  # Example: return half the length of the text as the size

    # Create an instance of the custom size estimator
    half_length_size_estimator = HalfLengthSizeEstimator()

    # Use the custom size estimator in a TextChunker
    text_chunker = RecursiveTextChunker(chunk_size=100, size_estimator=half_length_size_estimator)
    text = "This is a sample text that will be chunked using a custom size estimator."
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")