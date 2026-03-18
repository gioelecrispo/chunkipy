from chunkipy.language_detectors.base_language_detector import BaseLanguageDetector
from chunkipy.utils import import_dependencies


class LangdetectLanguageDetector(BaseLanguageDetector):
    """Detect language codes using the optional ``langdetect`` dependency."""

    def __init__(self):
        """Initialize the detector with lazy dependency loading."""
        self._langdetect_module = None

    def _get_langdetect_module(self):
        """Return the langdetect dependency module.

        This method can be overridden by subclasses for advanced integrations.
        """
        if self._langdetect_module is None:
            self._langdetect_module = import_dependencies(
                extra="langdetect",
                package_name="langdetect",
            )
        return self._langdetect_module

    def detect(self, text: str) -> str:
        """Return the ISO-like language code detected by ``langdetect``."""
        self._validate_text(text)
        langdetect = self._get_langdetect_module()
        return langdetect.detect(text)