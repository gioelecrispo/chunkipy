import logging
from typing import Generator, Iterable, List
from chunkipy.text_chunker.base_text_chunker import BaseTextChunker
from chunkipy.text_chunker.data_models import Chunk, Chunks, Overlap, TextPart
from chunkipy.text_splitters import *
from chunkipy.size_estimators import BaseSizeEstimator, WordSizeEstimator


DEFAULT_TEXT_SPLITTERS = [
    SemicolonTextSplitter(),
    ColonTextSplitter(),
    CommaTextSplitter(),
    WordTextSplitter()
]

class RecursiveTextChunker(BaseTextChunker):

    def __init__(self, chunk_size: int = None,
                size_estimator: BaseSizeEstimator = None,
                overlap_ratio: float = 0.0,
                text_splitters: List [BaseTextSplitter] = []):

        super().__init__(chunk_size, size_estimator, overlap_ratio)
        self.text_splitters = list(text_splitters) + DEFAULT_TEXT_SPLITTERS


    def split_text(self, text: str) -> Generator [TextPart, None, None]:
        """Split the provided text into smaller parts based on the configured text splitters and chunk size.
        This method uses a recursive approach to apply different text splitters until the text fits properly within the chunk size (based on the size estimator).

        Args:
            text (str): The text to be split.

        Yields:
            Generator [TextPart, None, None]: A generator yielding TextPart objects, each containing a piece of text and its estimated size.
        """
        split_strategy_idx = 0  # start with the highest strategy
        yield from self._validate_and_split(text, split_strategy_idx)
        
    def _validate_text(self, text: str):
        if text is None or not isinstance(text, str):
            raise ValueError(f"Text must be a non-empty string. Text type: {type(text)}")
        if not text.strip():
            raise ValueError("Text cannot be empty or whitespace only.")
            
    def _validate_and_split(self, text: str, split_strategy_idx: int) -> Generator [TextPart, None, None]:
        text_splitter = self.text_splitters[split_strategy_idx]
        logging.debug(f"Text Splitter: {text_splitter}")
        text_parts = text_splitter.split(text)

        for text_part in text_parts:
            text_part_size = self.size_estimator.estimate_size(text_part)

            if split_strategy_idx < len(self.text_splitters)-1 \
                    and text_part_size > self.chunk_size:
                yield from self._validate_and_split(text_part, split_strategy_idx+1)
            else:
                yield TextPart(text=text_part, size=text_part_size)
