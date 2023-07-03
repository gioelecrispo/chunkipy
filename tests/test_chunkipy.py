import re
import unittest

from chunkipy import TextChunker, TokenEstimator
from chunkipy.text_splitter import split_by_separator


class CustomTokenEstimator(TokenEstimator):
    def estimate_tokens(self, text):
        return len([t for t in text.split("-") if t != '' and ' '])


def split_by_dash(text):
    return split_by_separator(text, "-")


def split_on_space_and_dot(text):
    pattern = r'[ .]'
    return [t + x.group() for t, x in
            zip(re.split(pattern, text), re.finditer(pattern, text))
            if t + x.group() != '' and ' ']


class TestTextChunker(unittest.TestCase):

    def test_chunkize_short_text(self):
        text_chunker = TextChunker(chunk_size=100)
        text = "This is a short text."
        expected_chunks = ["This is a short text."]
        self.assertEqual(text_chunker.chunk(text), expected_chunks)

    def test_chunkize_text(self):
        text_chunker = TextChunker(chunk_size=30)
        text = "This is a short text. This is another phrase."
        expected_chunks = ["This is a short text.", "This is another phrase."]
        self.assertEqual(text_chunker.chunk(text), expected_chunks)

    def test_chunkize_long_text(self):
        text_chunker = TextChunker(chunk_size=110)
        text = "This is a very long text. " * 16
        expected_chunks = [" ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4),
                           " ".join(["This is a very long text."] * 4)]
        self.assertEqual(expected_chunks, text_chunker.chunk(text))

    def test_chunkize_tokenized_short_text(self):
        text_chunker = TextChunker(chunk_size=5, tokens=True)
        text = "This is a tokenized text."
        expected_chunks = ['This is a tokenized text.']
        self.assertEqual(expected_chunks, text_chunker.chunk(text))

    def test_chunkize_tokenized_text(self):
        text_chunker = TextChunker(chunk_size=5, tokens=True)
        text = "This is a tokenized text. This is another phrase."
        expected_chunks = ['This is a tokenized text.',
                           'This is another phrase.']
        self.assertEqual(expected_chunks, text_chunker.chunk(text))

    def test_chunkize_tokenized_text_custom_split_strategy(self):
        split_strategies = [split_on_space_and_dot]
        text_chunker = TextChunker(chunk_size=3, tokens=True, split_strategies=split_strategies)
        text = "This is a custom split strategy text."
        expected_chunks = ["This is a", "custom split strategy", "text."]
        self.assertEqual(expected_chunks, text_chunker.chunk(text))

    def test_chunkize_tokenized_text_custom_tokenizer_and_custom_split_strategy(self):
        split_strategies = [split_by_dash]
        text_chunker = TextChunker(chunk_size=2, tokens=True, token_estimator=CustomTokenEstimator(),
                                  split_strategies=split_strategies)
        text = "This-is-a-custom-tokenized-text."
        expected_chunks = ["This-is-", "a-custom-", "tokenized-text."]
        self.assertEqual(expected_chunks, text_chunker.chunk(text))

    def test_overlapping_less_than_max(self):
        # Initialize TextChunker with overlap_percent = 0.1
        text_chunker = TextChunker(50, tokens=True, overlap_percent=0.2)

        self.assertEqual(text_chunker.overlap_size, 10)

        # Set up test input
        text = "In this unit test, we are evaluating the overlapping functionality." \
               "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
               "goal is to ensure that overlapping chunks are generated correctly. For this purpose, we have chosen a " \
               "long text that exceeds 100 ChatGPT tokens. By setting the overlap_percent to 0.1, we expect the " \
               "generated chunks to have an overlap of approximately 10%. This will help us verify the effectiveness " \
               "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
               "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
               "for proper overlap. "

        # Generate chunks with overlapping
        chunks = text_chunker.chunk(text)

        # Assert the overlapping chunks
        expected_chunks = ['In this unit test, we are evaluating the overlapping functionality. '
                           'This is a feature of the TextChunker class, which is important for a proper context keeping. '
                           'The goal is to ensure that overlapping chunks are '
                           'generated correctly.',
                           'For this purpose, we have chosen a long text that exceeds 100 ChatGPT '
                           'tokens. By setting the overlap_percent to 0.1, we expect the generated '
                           'chunks to have an overlap of approximately 10%. This will help us verify the '
                           'effectiveness of the overlapping feature.',
                           'The TextChunker class should be able to handle this scenario and produce the '
                           "expected results. Let's proceed with running the test and asserting the "
                           'generated chunks for proper overlap.'
                           ]
        self.assertEqual(chunks, expected_chunks)

    def test_overlapping(self):
        # Initialize TextChunker with overlap_percent = 0.1
        text_chunker = TextChunker(50, tokens=True, overlap_percent=0.3)

        self.assertEqual(text_chunker.overlap_size, 15)

        # Set up test input
        text = "In this unit test, we are evaluating the overlapping functionality." \
               "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
               "goal is to ensure that overlapping chunks are generated correctly. For this purpose, we have chosen a " \
               "long text that exceeds 100 ChatGPT tokens. By setting the overlap_percent to 0.1, we expect the " \
               "generated chunks to have an overlap of approximately 10%. This will help us verify the effectiveness " \
               "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
               "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
               "for proper overlap. "

        # Generate chunks with overlapping
        chunks = text_chunker.chunk(text)

        # Assert the overlapping chunks
        expected_chunks = ['In this unit test, we are evaluating the overlapping functionality. This is '
                           'a feature of the TextChunker class, which is important for a proper '
                           'context keeping. The goal is to ensure that overlapping chunks are generated '
                           'correctly.',
                           'The goal is to ensure that overlapping chunks are generated correctly. For '
                           'this purpose, we have chosen a long text that exceeds 100 ChatGPT tokens. By '
                           'setting the overlap_percent to 0.1, we expect the generated chunks to have '
                           'an overlap of approximately 10%.',
                           'This will help us verify the effectiveness of the overlapping feature. The '
                           'TextChunker class should be able to handle this scenario and produce the '
                           "expected results. Let's proceed with running the test and asserting the "
                           'generated chunks for proper overlap.']
        self.assertEqual(chunks, expected_chunks)


if __name__ == '__main__':
    unittest.main()
