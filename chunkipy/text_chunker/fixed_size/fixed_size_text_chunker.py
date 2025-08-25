import logging
from typing import Generator, Iterable, List
from chunkipy.text_chunker.base_text_chunker import BaseTextChunker
from chunkipy.text_chunker.data_models import Chunk, Chunks, Overlap, TextPart
from chunkipy.text_splitters import *
from chunkipy.size_estimators import BaseSizeEstimator, WordSizeEstimator



class FixedSizeTextChunker(BaseTextChunker):

    def __init__(self, chunk_size: int = None,
                size_estimator: BaseSizeEstimator = None,
                overlap_ratio: float = 0.0):
        super().__init__(chunk_size, size_estimator, overlap_ratio)

    def split_text(self, text: str) -> Generator [TextPart, None, None]:
        """Split the provided text into smaller parts based on size estimator. 
        Size Estimator is used to cut the text into segments and every segment has size equal to 1.

        Args:
            text (str): The text to be split.

        Yields:
            Generator [TextPart, None, None]: A generator yielding TextPart objects, each containing a piece of text and its estimated size.
        """
        text_segments = self.size_estimator.segment(text)
        for text_segment in text_segments:
            yield TextPart(text=text_segment, size=1)
        