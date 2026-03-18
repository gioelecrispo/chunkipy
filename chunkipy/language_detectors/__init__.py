"""Public language detector classes exposed by :mod:`chunkipy.language_detectors`."""

from chunkipy.language_detectors.base_language_detector import BaseLanguageDetector
from chunkipy.language_detectors.langdetect_language_detector import LangdetectLanguageDetector
from chunkipy.language_detectors.fasttext_language_detector import FastTextLanguageDetector


__all__ = [
    "BaseLanguageDetector",
    "LangdetectLanguageDetector",
    "FastTextLanguageDetector",
]