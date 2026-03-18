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
        return f"{self.__class__.__name__}(size={self.size}, elements={list(self)})"





class TextParts (TextPartsMixin, List[TextPart]):
    """List-like collection of :class:`TextPart` values.

    This container preserves the normal ``list`` API while exposing aggregated
    ``size`` and ``text`` properties via :class:`TextPartsMixin`.
    """
    pass


class Overlap (TextPartsMixin, Deque[TextPart]):
    """Deque-like collection used to carry overlap between consecutive chunks."""
    pass



@dataclass
class Chunk:
    """Single chunk returned by a text chunker.

    A chunk is composed of two ordered collections:

    - ``overlap``: text parts repeated from the previous chunk to preserve context
    - ``content``: text parts that are unique to the current chunk

    The ``text`` and ``size`` properties are computed over the combined
    ``text_parts`` view.
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
        """Return a combined ordered view of overlap and content text parts."""
        return TextParts (chain(self.overlap, self.content))

    def __repr__(self) -> str:
        return f"Chunk(size={self.size}, text='{self.text}', overlap={self.overlap}, content={self.content})"
        

class Chunks(List[Chunk]):
    """List-like collection of :class:`Chunk` objects returned by chunkers."""

    def get_all_text_parts(self) -> List[List[str]]:
        """Return the text parts for every chunk.

        Returns:
            List[List[str]]: A list of per-chunk text part collections.
        """
        return [chunk.text_parts for chunk in self]


    def get_all_text(self) -> List[str]:
        """Return the serialized text for every chunk.
        
        Returns:
            List[str]: A list of strings, where each string is the full text of a chunk.
        """
        return [chunk.text for chunk in self]



