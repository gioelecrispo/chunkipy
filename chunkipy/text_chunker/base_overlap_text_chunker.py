from abc import ABC, abstractmethod
from typing import Generator, Iterable

from chunkipy.text_chunker.base_text_chunker import BaseTextChunker
from chunkipy.text_chunker.data_models import Chunk, Chunks, Overlap, TextPart
from chunkipy.size_estimators import BaseSizeEstimator


class BaseOverlapTextChunker(BaseTextChunker, ABC):
    """Base class for chunkers that assemble chunks with overlap from text parts."""

    def __init__(
        self,
        chunk_size: int = None,
        size_estimator: BaseSizeEstimator = None,
        overlap_ratio: float = 0.0,
    ):
        """Initialize overlap-aware chunker settings.

        Args:
            chunk_size: Maximum chunk size in estimator units.
            size_estimator: Strategy used to estimate text part sizes.
            overlap_ratio: Ratio of ``chunk_size`` to preserve as overlap between
                consecutive chunks. Must be between ``0.0`` and ``1.0``.
        """
        if overlap_ratio < 0 or overlap_ratio > 1:
            raise ValueError(
                f"overlap_ratio must be between 0 and 1. Current value: {overlap_ratio}"
            )

        super().__init__(chunk_size=chunk_size, size_estimator=size_estimator)
        self.overlap_size = int(self.chunk_size * overlap_ratio)
        self.overlap_enabled = self.overlap_size > 0

    def chunk(self, text: str) -> Chunks:
        """Chunk text by splitting first and then assembling chunk objects."""
        self._validate_text(text)
        text_parts = self.split_text(text)
        return self._build_chunks(text_parts)

    def _build_chunks(self, text_parts: Iterable[TextPart]) -> Chunks:
        """Assemble a stream of text parts into chunk objects with overlap."""
        chunks = Chunks()
        curr_chunk = Chunk()
        overlap = Overlap()

        for text_part in text_parts:
            if curr_chunk.size + text_part.size <= self.chunk_size:
                curr_chunk.content.append(text_part)

                if self.overlap_enabled:
                    while overlap.size + text_part.size > self.overlap_size and overlap:
                        overlap.popleft()
            else:
                chunks.append(curr_chunk)
                curr_chunk = Chunk()

                if self.overlap_enabled:
                    curr_chunk.overlap = overlap
                    overlap = Overlap()

                curr_chunk.content.append(text_part)

            if text_part.size <= self.overlap_size:
                overlap.append(text_part)

        chunks.append(curr_chunk)
        return chunks

    @abstractmethod
    def split_text(self, text: str) -> Generator[TextPart, None, None]:
        """Split text into parts consumed by overlap-aware chunk assembly."""
        raise NotImplementedError("Subclasses must implement split_text method.")
