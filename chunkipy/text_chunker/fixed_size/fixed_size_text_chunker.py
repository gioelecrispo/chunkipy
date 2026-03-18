from typing import Generator
from chunkipy.text_chunker.base_overlap_text_chunker import BaseOverlapTextChunker
from chunkipy.text_chunker.data_models import TextPart
from chunkipy.size_estimators import BaseSizeEstimator


class FixedSizeTextChunker(BaseOverlapTextChunker):
    """Chunk text into fixed-size slices using the configured size estimator.

    Each segment emitted by ``size_estimator.segment`` is treated as a unit of
    size ``1`` during chunk assembly.
    """

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
        