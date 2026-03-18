from chunkipy.size_estimators import WordSizeEstimator


if __name__ == "__main__":
    text = "Chunkipy estimates by words in this simple sentence."
    estimator = WordSizeEstimator()

    print(f"Estimated size: {estimator.estimate_size(text)}")
    print("Segments:", list(estimator.segment(text)))
