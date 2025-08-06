from abc import abstractmethod
from typing import List
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


class BaseSemanticTextSplitter(BaseTextSplitter):
    """
    Base class for semantic text splitters.
    This class extends BaseTextSplitter and provides a framework for splitting
    text into semantic parts. 

    text_limit attribute helps to control input size for semantic models, that might fail with long texts.
    It is used to limit the size of text processed at once, which is useful for semantic models that may have constraints on input size.
    text_limit does not affect the splitting logic, but rather the size of the text that is passed to the _split method. 
    For example, if your text is 3500 chars and is text_limit is set to 1000, the text will be split into 4 parts of at most 1000 characters before being passed to the _split method.
    
    Args:
        text_limit (int): The maximum length of text to be processed at once.
        If None, defaults to a large value (1,000,000 characters).
    Attributes:
        text_limit (int): The maximum length of text to be processed at once.
        DEFAULT_TEXT_LIMIT (int): Default value for text_limit if not provided.
    Raises:
        NotImplementedError: If the _split method is not implemented in a subclass.
        
    """
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
            j = i - len_last_part
            partial_text = text[j : i + self.text_limit]
            text_parts.extend(self._split(partial_text))
            if i < (len(text) - self.text_limit):  # if it's not the last iteration
                # Find the index of the last split part within the partial_text, starting from the end.
                # This ensures we account for delimiters, spaces, or any semantic split logic.
                last_part = text_parts.pop() if text_parts else ""
                # Search for the last_part at the end of partial_text
                idx = partial_text.rfind(last_part)
                if idx != -1:
                    # Compute the length of the last part based on its position in partial_text
                    # This ensures that we correctly handle cases where the last part is not at the end of partial_text
                    # (because of spaces, delimiters, or anything else) and we need to adjust the length accordingly.
                    len_last_part = len(partial_text) - idx
                else:
                    # Fallback: use the length of last_part
                    len_last_part = len(last_part)

        return text_parts