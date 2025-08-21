import logging
from typing import Generator, Iterable, List
from chunkipy.text_chunker.data_models import Chunk, Chunks, Overlap, TextPart
from chunkipy.text_splitters import *
from chunkipy.size_estimators import BaseSizeEstimator, WordSizeEstimator


DEFAULT_CHUNK_SIZE = 1000  

DEFAULT_TEXT_SPLITTERS = [
    SemicolonTextSplitter(),
    ColonTextSplitter(),
    CommaTextSplitter(),
    WordTextSplitter()
]

class TextChunker:

    def __init__(self, chunk_size: int = None,
                size_estimator: BaseSizeEstimator = None,
                overlap_ratio: float = 0.0,
                text_splitters: List [BaseTextSplitter] = []):

        if overlap_ratio < 0 or overlap_ratio > 1:
            raise ValueError(f"overlap_ratio must be between 0 and 1. Current value: {overlap_ratio}")

        if chunk_size and not isinstance(chunk_size, int):
            raise ValueError(f"chunk_size must be between a positive integer. Current value: {chunk_size}")

        self.chunk_size = chunk_size if chunk_size is not None else DEFAULT_CHUNK_SIZE
        self.overlap_size = int(self.chunk_size * overlap_ratio)
        self.overlap_enabled = True if self.overlap_size > 0 else False
        self.size_estimator = size_estimator

        if size_estimator is None:
            self.size_estimator = WordSizeEstimator()
        
        self.text_splitters = list(text_splitters) + DEFAULT_TEXT_SPLITTERS

    def chunk(self, text: str) -> Chunks:
        """ Chunk the provided text into smaller parts based on the configured chunk size and overlap.
        
        Args:
            text (str): The text to be chunked

        Returns:
            Chunks: A list containing the chunks and for each chunks the list of text parts the made it up.
        """
        self._validate_text(text)
        text_parts_and_counts = self.split_text(text)
        return self._build_chunks(text_parts_and_counts)

    def split_text(self, text: str) -> Generator [TextPart, None, None]:
        """ Split the provided text into smaller parts based on the configured text splitters and chunk size.

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

    def _build_chunks(self, text_parts: Iterable[TextPart]) -> Chunks:
        chunks = Chunks()
        curr_chunk = Chunk()  # Current chunk to accumulate text_parts
        overlap = Overlap()  # Sliding deque of overlapping text_parts

        for text_part in text_parts:
            # Add text_part to the current chunk if it fits within the chunk size
            if curr_chunk.size + text_part.size <= self.chunk_size:
                curr_chunk.content.append(text_part)

                # Handle overlapping text_parts if overlap is configured
                if self.overlap_enabled:
                    while overlap.size + text_part.size > self.overlap_size and overlap: 
                        overlap.popleft() # Remove text_parts from the left until size fits

            else: # Chunk size exceeded, finalize the current chunk and create a new one
                chunks.append(curr_chunk)
                curr_chunk = Chunk()

                if self.overlap_enabled:
                    # move current overlap to new curr chunk and reset overlap
                    curr_chunk.overlap = overlap
                    overlap = Overlap()
                
                curr_chunk.content.append(text_part)

            # Add the text_part to the overlapping deque if it fits within the overlap size
            if text_part.size <= self.overlap_size:
                overlap.append(text_part)

        # Add the final chunk after the loop ends
        chunks.append(curr_chunk)
        return chunks
