from chunkipy.size_estimators import OpenAISizeEstimator
from chunkipy.utils import MissingDependencyError


if __name__ == "__main__":
    text = "Token-aware estimation with tiktoken."

    try:
        estimator = OpenAISizeEstimator()
        print(f"Estimated token size: {estimator.estimate_size(text)}")
    except MissingDependencyError as error:
        print(error)
