import os

from chunkipy.language_detectors import FastTextLanguageDetector
from chunkipy.utils import MissingDependencyError


if __name__ == "__main__":
    model_path = os.getenv("FASTTEXT_MODEL_PATH")

    if not model_path:
        print("Set FASTTEXT_MODEL_PATH to run this example with a local FastText model.")
        raise SystemExit(0)

    try:
        detector = FastTextLanguageDetector(model_path=model_path)
        print(f"Detected language: {detector.detect('This text is written in English.')}")
    except MissingDependencyError as error:
        print(error)
