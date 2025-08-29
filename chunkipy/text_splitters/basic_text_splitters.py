from typing import List
from typing_extensions import override
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter


class SeparatorTextSplitter(BaseTextSplitter):

    def __init__(self, separator: str):
        if not separator or not isinstance (separator, str):
            raise ValueError("Provide a valid non-empty separator.")
        self._separator = separator

    @property
    def separator(self) -> str:
        return self._separator
    
    @override
    def _split(self, text: str) -> List[str]:
        text_pieces = text.split(self.separator)
        text_pieces = [t + self.separator for t in text_pieces if t != ' ' and t != '']
        text_pieces[-1] = text_pieces[-1][:-len(self.separator)]
        return text_pieces


class SemicolonTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator="; ")


class ColonTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator=": ")


class CommaTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator=", ")
        

class FullStopTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator=". ")
        

class NewlineTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator="\n")
        

class WordTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator=" ")