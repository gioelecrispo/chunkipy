from typing import Callable, List

from chunkipy.text_splitter import *


SPLIT_STRATEGIES = (
    split_by_sentences,
    split_by_semicolon,
    split_by_colon,
    split_by_comma,
    split_by_word
)


class TextChunkizer:

    DEFAULT_CHUNK_SIZE = 1000  # chars or tokens, based on tokens flag

    def __init__(self, chunk_size: int = DEFAULT_CHUNK_SIZE,
                 tokens: bool = False,
                 tokenizer_func: Callable = None,
                 split_strategies: List[Callable] = SPLIT_STRATEGIES):
        self.chunk_size = chunk_size  # chars or tokens, based on tokens flag
        self.tokens = tokens  # segment by tokens if true, chars otherwise
        self.tokenizer_func = tokenizer_func  # tokenizer function, which returns a list of tokens
        self.split_strategies = split_strategies

    def chunkize(self, text):
        text_parts = []
        text_elem = text if self.tokens is False \
            else self._set_tokenizer_function(text)
        if len(text_elem) > self.chunk_size:
            chunks = self.segment(text)
            text_parts += chunks
        else:
            text_parts += [text]
        return text_parts

    def segment(self, text):
        if self.tokens is False:
            return self._split_text_and_build_chunks(text, elem_funct=None)
        return self._split_text_and_build_chunks(text, elem_funct=self._set_tokenizer_function)

    def _set_tokenizer_function(self, text):
        if self.tokenizer_func is None:
            return default_tokenizer(text)
        return self.tokenizer_func(text)

    def _split_text_and_build_chunks(self, text, elem_funct=None):
        text_parts_and_counts = self._split_text(text, elem_funct)
        return self._build_chunks(text_parts_and_counts)

    def _split_text(self, text, elem_funct):
        text_parts_and_counts = []
        split_strategy = 0
        self._validate_and_split(text, elem_funct,
                                 split_strategy,
                                 text_parts_and_counts)
        return text_parts_and_counts

    def _validate_and_split(self, text, elem_funct, split_strategy,
                            total_text_parts_and_counts):
        funct = self.split_strategies[split_strategy]
        logging.debug(f"Split Strategy: {funct}")
        text_parts = funct(text)
        for i, text_part in enumerate(text_parts):
            text_part_elem = text_part if elem_funct is None \
                else elem_funct(text_part)
            elements_count_in_text_part = len(text_part_elem)

            if split_strategy < len(self.split_strategies)-1 \
                    and elements_count_in_text_part > self.chunk_size:
                self._validate_and_split(text_part,
                                         elem_funct,
                                         split_strategy+1,
                                         total_text_parts_and_counts)
            else:
                total_text_parts_and_counts.append((text_part,
                                                    elements_count_in_text_part))

    def _build_chunks(self, text_parts_and_counts):
        chunks = []
        chunk_element_count = 0
        chunk = ""
        for text_part, elements_count in text_parts_and_counts:
            if chunk_element_count + elements_count <= self.chunk_size:
                chunk_element_count += elements_count
                chunk += text_part
            else:
                chunks.append(chunk.strip())
                chunk_element_count = elements_count
                chunk = text_part
        chunks.append(chunk.strip())
        return [chunk for chunk in chunks if chunk != '' and ' ']

