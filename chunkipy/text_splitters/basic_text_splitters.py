from typing import List
from typing_extensions import override
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


class SeparatorTextSplitter(BaseTextSplitter):
    """Split text using a fixed separator while preserving the separator."""

    def __init__(self, separator: str):
        """Initialize the splitter with the delimiter to preserve in output."""
        if not separator or not isinstance (separator, str):
            raise ValueError("Provide a valid non-empty separator.")
        self._separator = separator

    @property
    def separator(self) -> str:
        """Return the delimiter used by the splitter."""
        return self._separator
    
    @override
    def _split(self, text: str) -> List[str]:
        text_pieces = text.split(self.separator)
        text_pieces = [t + self.separator for t in text_pieces if t != ' ' and t != '']
        text_pieces[-1] = text_pieces[-1][:-len(self.separator)]
        return text_pieces


class SemicolonTextSplitter(SeparatorTextSplitter):
    """Split text on ``; `` boundaries."""

    def __init__(self):
        super().__init__(separator="; ")


class ColonTextSplitter(SeparatorTextSplitter):
    """Split text on ``: `` boundaries."""

    def __init__(self):
        super().__init__(separator=": ")


class CommaTextSplitter(SeparatorTextSplitter):
    """Split text on ``, `` boundaries."""

    def __init__(self):
        super().__init__(separator=", ")
        

class FullStopTextSplitter(SeparatorTextSplitter):
    """Split text on ``. `` sentence-like boundaries."""

    def __init__(self):
        super().__init__(separator=". ")
        

class NewlineTextSplitter(SeparatorTextSplitter):
    """Split text on newline boundaries."""

    def __init__(self):
        super().__init__(separator="\n")
        

class WordTextSplitter(SeparatorTextSplitter):
    """Split text on spaces while preserving trailing whitespace."""

    def __init__(self):
        super().__init__(separator=" ")