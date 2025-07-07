from collections import deque
from dataclasses import dataclass, field
from typing import List

@dataclass
class TextPart:
    """Represents a fragment or segment of a complete text, along with its character size.

    :param text: The text of the segment.
    :param size: The size of the text in characters.
    """
    text: str
    size: int


@dataclass  
class Chunk:
    """Represents a single chunk of text, which consists of multiple text parts.
    
    Computed Properties:
    :param text: Represents the full text of the chunk by joining all 'text' values from its 'text parts.
    :param text:parts: A list of TextPart objects that make up the chunk.
    """
    text_parts: List[TextPart] = field(default_factory=list)  # Ensure proper initialization


    @property
    def text(self) -> str:
        """Returns the full concatenated text of the chunk by joining all 'text' values from the TextPart objects.

        Returns:
            str: The full text of the chunk, concatenated from all text parts.
        """
        return ''.join(part.text for part in self.text_parts).strip()


    @property
    def size(self) -> int:
        """Calculates and returns the total size of all TextPart objects within text_parts.

        Returns:
        int: The total size of all TextPart objects.
        """
        return sum(part.size for part in self.text_parts) if self.text_parts else 0
    

    def __repr__(self) -> str:
        return (f"Chunk(text='{self.text}', size={self.size}, "
                f"text_parts={self.text_parts})")


class Chunks(list):
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


class Overlapping(deque):
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
        return f"Overlapping(size={self.size}, elements={list(self)})"
