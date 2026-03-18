from abc import ABC, abstractmethod


class BaseLanguageDetector(ABC):
    """Base class for strategies that detect the language of a text."""

    def _validate_text(self, text: str) -> None:
        """Validate the text passed to :meth:`detect`."""
        if text is None or not isinstance(text, str):
            raise TypeError(f"Text must be a non-empty string. Current value: {text}")
        if not text.strip():
            raise ValueError("Text cannot be empty or whitespace only.")

    @abstractmethod
    def detect(self, text: str) -> str:
        """Detect the language code for the given text."""
        raise NotImplementedError("Subclasses must implement the detect method.")