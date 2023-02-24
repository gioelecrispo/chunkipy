import re
import unittest

from chunkipy import TextChunkizer
from chunkipy.text_splitter import split_by_separator


def custom_tokenizer(text):
    return [t for t in text.split("-") if t != '' and ' ']


def split_by_dash(text):
    return split_by_separator(text, "-")


def split_on_space_and_dot(text):
    pattern = r'[ .]'
    return [t + x.group() for t, x in
            zip(re.split(pattern, text), re.finditer(pattern, text))
            if t + x.group() != '' and ' ']


class TestTextChunkizer(unittest.TestCase):

    def test_chunkize_short_text(self):
        chunkizer = TextChunkizer(chunk_size=100)
        text = "This is a short text."
        expected_chunks = ["This is a short text."]
        self.assertEqual(chunkizer.chunkize(text), expected_chunks)

    def test_chunkize_text(self):
        chunkizer = TextChunkizer(chunk_size=30)
        text = "This is a short text. This is another phrase."
        expected_chunks = ["This is a short text.", "This is another phrase."]
        self.assertEqual(chunkizer.chunkize(text), expected_chunks)

    def test_chunkize_long_text(self):
        chunkizer = TextChunkizer(chunk_size=110)
        text = "This is a very long text. " * 16
        expected_chunks = [" ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4)]
        self.assertEqual(expected_chunks, chunkizer.chunkize(text))

    def test_chunkize_tokenized_short_text(self):
        chunkizer = TextChunkizer(chunk_size=5, tokens=True)
        text = "This is a tokenized text."
        expected_chunks = ['This is a tokenized text.']
        self.assertEqual(expected_chunks, chunkizer.chunkize(text))

    def test_chunkize_tokenized_text(self):
        chunkizer = TextChunkizer(chunk_size=5, tokens=True)
        text = "This is a tokenized text. This is another phrase."
        expected_chunks = ['This is a tokenized text.',
                           'This is another phrase.']
        self.assertEqual(expected_chunks, chunkizer.chunkize(text))

    def test_chunkize_tokenized_text_custom_split_strategy(self):
        split_strategies = [split_on_space_and_dot]
        chunkizer = TextChunkizer(chunk_size=3, tokens=True,
                                  split_strategies=split_strategies)
        text = "This is a custom split strategy text."
        expected_chunks = ["This is a", "custom split strategy", "text."]
        self.assertEqual(expected_chunks, chunkizer.chunkize(text))

    def test_chunkize_tokenized_text_custom_tokenizer_and_custom_split_strategy(self):
        split_strategies = [split_by_dash]
        chunkizer = TextChunkizer(chunk_size=2, tokens=True,
                                  split_strategies=split_strategies,
                                  tokenizer_func=custom_tokenizer)
        text = "This-is-a-custom-tokenized-text."
        expected_chunks = ["This-is-", "a-custom-", "tokenized-text."]
        self.assertEqual(expected_chunks, chunkizer.chunkize(text))


if __name__ == '__main__':
    unittest.main()