from collections import deque
from typing import Callable, List

from chunkipy.text_splitter import *
from chunkipy.tokens_estimators import TokenEstimator, WordTokenEstimator, CharTokenEstimator

SPLIT_STRATEGIES = (
    split_by_sentences,
    split_by_semicolon,
    split_by_colon,
    split_by_comma,
    split_by_word
)


class TextChunker:

    DEFAULT_CHUNK_SIZE = 1000  # chars or tokens, based on tokens flag

    def __init__(self, chunk_size: int = DEFAULT_CHUNK_SIZE,
                 tokens: bool = False,
                 token_estimator: TokenEstimator = WordTokenEstimator(),
                 overlap_percent: float = 0.0,
                 split_strategies: List[Callable] = SPLIT_STRATEGIES):
        self.chunk_size = chunk_size  # chars or tokens, based on tokens flag
        self.overlap_size = int(chunk_size*overlap_percent)
        self.tokens = tokens  # segment by tokens if true, chars otherwise
        self.token_estimator = token_estimator if tokens is True else CharTokenEstimator()
        self.split_strategies = split_strategies

    def chunk(self, text):
        text_parts = []
        text_elem_count = self.token_estimator.estimate_tokens(text)
        if text_elem_count > self.chunk_size:
            chunks = self._split_text_and_build_chunks(text)
            text_parts.extend(chunks)
        else:
            text_parts.append(text)
        return text_parts

    def _split_text_and_build_chunks(self, text):
        text_parts_and_counts = self.split_text(text)
        return self._build_chunks(text_parts_and_counts)

    def split_text(self, text):
        split_strategy = 0
        yield from self._validate_and_split(text, split_strategy)

    def _validate_and_split(self, text, split_strategy):
        split_funct = self.split_strategies[split_strategy]
        logging.debug(f"Split Strategy: {split_funct}")
        text_parts = split_funct(text)
        for i, text_part in enumerate(text_parts):
            elements_count_in_text_part = self.token_estimator.estimate_tokens(text_part)

            if split_strategy < len(self.split_strategies)-1 \
                    and elements_count_in_text_part > self.chunk_size:
                yield from self._validate_and_split(text_part, split_strategy+1)
            else:
                yield text_part, elements_count_in_text_part

    def _build_chunks(self, text_parts_and_counts):
        chunks = []

        chunk_element_count = 0
        chunk = []
        overlap_count = 0
        overlapping = deque()

        for text_part, elements_count in text_parts_and_counts:
            if chunk_element_count + elements_count <= self.chunk_size:
                chunk_element_count += elements_count
                chunk.append(text_part)
                if self.overlap_size > 0:
                    while overlap_count + elements_count > self.overlap_size and overlapping:
                        _, first_overlapping_count = overlapping.popleft()
                        overlap_count -= first_overlapping_count
            else:
                chunks.append("".join(chunk).strip())
                chunk_element_count = 0
                chunk = []
                if self.overlap_size > 0:
                    overlapping_text = "".join([t[0] for t in overlapping])
                    chunk_element_count = overlap_count
                    chunk = [overlapping_text]
                    overlap_count = 0
                    overlapping = deque()

                chunk_element_count += elements_count
                chunk += text_part

            if elements_count <= self.overlap_size:
                overlap_count += elements_count
                overlapping.append((text_part, elements_count))

        chunks.append("".join(chunk).strip())
        return chunks

