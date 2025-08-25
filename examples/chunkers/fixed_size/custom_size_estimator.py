from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator
from chunkipy import FixedSizeTextChunker


if __name__ == "__main__":
    # For FixedSizeTextChunker implementation of segment method in SizeEstimator is mandatory
     
    class CommaSizeEstimator(BaseSizeEstimator):
        def estimate_size(self, text):
            # Implement your custom size estimation logic here
            return len(text.split(","))  # Example: return the number of segment separated by commas as the size

        def segment(self, text):
            # Implement your custom segmentation logic here
            return text.split(",")

    # Create an instance of the custom size estimator
    comma_size_estimator = CommaSizeEstimator()

    # Use the custom size estimator in a TextChunker
    text_chunker = FixedSizeTextChunker(chunk_size=100, size_estimator=comma_size_estimator)
    text = "This is a sample text, that will be chunked using a custom size estimator, expected size is therefore 3."
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")