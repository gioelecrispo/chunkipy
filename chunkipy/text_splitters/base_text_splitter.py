from abc import ABC, abstractmethod


class BaseTextSplitter(ABC):
    """Base class for splitter strategies that divide text into smaller pieces."""

    def split(self, text: str) -> list[str]:
        """
        Template method for splitting text. Validates the input and delegates
        the actual splitting logic to the subclass.
        
        Args:
            text (str): The text to be split.

        Returns:
            list[str]: A list of text text parts.
        """
        self._validate_text(text) 
        return self._split(text)  

    def _validate_text(self, text: str):
        """Validate the input text passed to :meth:`split`."""
        if text is None or not isinstance(text, str):
            raise TypeError(f"Text must be a non-empty string. Current value: {text}")
        if not text.strip():
            raise ValueError("Text cannot be empty or whitespace only.")

    @abstractmethod
    def _split(self, text: str) -> list[str]:
        """
        Abstract method for subclasses to implement specific splitting logic.

        Args:
            text (str): The text to be split.

        Returns:
            list[str]: A list of text text parts.
        """
        raise NotImplementedError("Subclasses must implement the split method.")