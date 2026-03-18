from chunkipy.size_estimators import CharSizeEstimator


if __name__ == "__main__":
    text = "Chunkipy estimates by characters."
    estimator = CharSizeEstimator()

    print(f"Estimated size: {estimator.estimate_size(text)}")
    print("First 10 segments:", list(estimator.segment(text))[:10])
