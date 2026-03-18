from chunkipy.language_detectors import LangdetectLanguageDetector
from chunkipy.utils import MissingDependencyError


if __name__ == "__main__":
    text = "Questo testo è scritto in italiano."

    try:
        detector = LangdetectLanguageDetector()
        print(f"Detected language: {detector.detect(text)}")
    except MissingDependencyError as error:
        print(error)
