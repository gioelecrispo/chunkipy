from abc import abstractmethod
from typing import List
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


class BaseTextSemanticSplitter(BaseTextSplitter):
    DEFAULT_TEXT_LIMIT = 1000000

    def __init__(self, text_limit: int = None):
        self.text_limit = text_limit or self.DEFAULT_TEXT_LIMIT

    @abstractmethod
    def _split(self, text: str) -> List[str]:
        raise NotImplementedError("Subclasses must implement the _split method.")


    def split(self, text: str) -> List[str]:
        """Split the given text into text parts based on semantic rules.
        This method overrides the split method from BaseTextSplitter and uses the
        _split method to perform the actual splitting. It handles large texts by
        breaking them into smaller chunks based on the text_limit attribute.
        This method ensures that the text is split into manageable parts while
        preserving semantic meaning.
        
        Args:
            text (str): The text to be split.
        Returns:
            List[str]: A list of text parts.
        """
        super()._validate_text(text)
        text_parts = []
        len_last_part = 0

        for i in range(0, len(text), self.text_limit):
            partial_text = text[i - len_last_part : i + self.text_limit].strip()
            text_parts.extend(self._split(partial_text))
            if i < (len(text) - self.text_limit): # if it's not the last iteration
                len_last_part = len(text_parts.pop())

        return text_parts