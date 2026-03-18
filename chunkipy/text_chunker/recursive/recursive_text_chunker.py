import logging
from typing import Generator, List
from chunkipy.text_chunker.base_overlap_text_chunker import BaseOverlapTextChunker
from chunkipy.text_chunker.data_models import TextPart
from chunkipy.text_splitters import (
    BaseTextSplitter, SemicolonTextSplitter, ColonTextSplitter,
    CommaTextSplitter, WordTextSplitter,
)
from chunkipy.size_estimators import BaseSizeEstimator


DEFAULT_TEXT_SPLITTERS = [
    SemicolonTextSplitter(),
    ColonTextSplitter(),
    CommaTextSplitter(),
    WordTextSplitter()
]

class RecursiveTextChunker(BaseOverlapTextChunker):
    """Chunk text by recursively applying increasingly fine-grained splitters.

    The chunker tries each splitter in order until a text part fits within the
    configured ``chunk_size``. Custom splitters are attempted before the default
    fallback splitters.
    """

    def __init__(self, chunk_size: int = None,
                size_estimator: BaseSizeEstimator = None,
                overlap_ratio: float = 0.0,
                text_splitters: List[BaseTextSplitter] = None):
        """Initialize a recursive chunker.

        Args:
            chunk_size: Maximum chunk size in estimator units.
            size_estimator: Strategy used to measure text size.
            overlap_ratio: Overlap ratio between chunks.
            text_splitters: Optional custom splitters to prepend to the default
                recursive splitting chain.
        """

        super().__init__(chunk_size, size_estimator, overlap_ratio)
        self.text_splitters = list(text_splitters or []) + DEFAULT_TEXT_SPLITTERS


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
        
    def _validate_and_split(self, text: str, split_strategy_idx: int) -> Generator [TextPart, None, None]:
        """Recursively split a text part until it fits within the chunk size."""
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
