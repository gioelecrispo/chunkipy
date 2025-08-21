from collections import deque
from dataclasses import dataclass, field
from itertools import chain
from typing import Deque, List

@dataclass
class TextPart:
    """Represents a fragment or segment of a complete text, along with its character size.

    :param size: The size of the text based on the SizeEstimator used.
    :param text: The text of the segment.
    """
    size: int
    text: str



class TextPartsMixin:
    """A base class with utilities for handling collections of TextPart."""

    @property
    def size(self) -> int:
        """Calculates the total size of all TextPart objects in the collection.
        
        Returns:
            int: The total size of all TextPart objects.
        """
        return sum(text_part.size for text_part in self)

    @property
    def text(self) -> str:
        """Concatenates and returns the full text of all TextParts in the collection.

        Returns:
            str: A single string containing the concatenated text of all TextParts.
        """
        return ''.join(text_part.text for text_part in self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self.size}, elements={list(self)}"





class TextParts (TextPartsMixin, List[TextPart]):
    """A list-like collection of TextParts.
    Inherits from list to act as a standard list, and from TextPartsMixin to provide additional methods for aggregated operations (e.g. size, text).
    """
    pass


class Overlap (TextPartsMixin, Deque [TextPart]):
    """A deque-like collection of TextParts with utility methods for aggregation.
    Inherits from deque to act as a standard deque, and from TextParts to provide additional methods for aggregated operations (e.g. size, text).
    """
    pass



@dataclass
class Chunk:
    """Represents a single chunk of text, which consists of multiple text parts.

    Computed Properties:
    :param text: Represents the full text of the chunk by joining all 'text' values from its 'text parts.
    :param overlap: A list of TextPart objects that make up the chunk.
    :param content: A list of TextPart objects that make up the chunk.
    """

    overlap: Overlap = field(default_factory=Overlap) # Ensure proper initialization
    content: TextParts = field(default_factory=TextParts) # Ensure proper initialization


    @property
    def size(self) -> int:
        """Calculates and returns the total size of all TextPart objects within text_parts.
        
        Returns:
            int: The total size of all TextPart objects.
        """
        return self.text_parts.size

    @property
    def text(self) -> str:
        """Returns the full concatenated text of the chunk by joining all 'text' values from the TextPart objects.

        Returns:
            str: The full text of the chunk, concatenated from all text parts.
        """
        return self.text_parts.text
    
    @property
    def text_parts(self) -> TextParts:
        """Returns the full concatenated text of the chunk by joining all 'text' values from the TextPart objects.

        Returns:
            str: The full text of the chunk, concatenated from all text parts.
        """
        return TextParts (chain(self.overlap, self.content))

    def __repr__(self) -> str:
        return f"Chunk(size={self.size}, text='{self.text}, overlap={self.overlap}, content={self.content}"
        

class Chunks(List[Chunk]):
    """A list-like collection of chunks with utility methods for aggregation.

    Inherits from 'list' to act as a standard list, while providing additional methods for aggregated operations.
    """

    def get_all_text_parts(self) -> List[List[str]]:
        """Returns all text parts from each chunk as a list of lists.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains the text parts of a chunk.
        """
        return [chunk.text_parts for chunk in self]


    def get_all_text(self) -> List[str]:
        """Returns the full text from all chunks as a list.
        
         Returns:
            List[str]: A list of strings, where each string is the full text of a chunk.
        """
        return [chunk.text for chunk in self]


class Overlap(Deque[TextPart]):
    """A deque-like collection of TextParts with utility methods for aggregation.
    Inherits from deque to act as a standard deque, while providing additional
    methods for aggregated operations (e.g. size).
    """
    
    @property
    def size(self) -> str:
        """Calculates and returns the total size of all TextPart objects.
        
        Returns:
            int: The total size of all TextPart objects.
        """
        return sum(part.size for part in self) if self else 0

    def __repr__(self) -> str:
        return f"Overlap(size={self.size}, elements={list(self)})"
