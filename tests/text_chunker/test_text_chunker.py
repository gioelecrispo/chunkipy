import unittest

from chunkipy import TextChunker
from chunkipy.size_estimators import BaseSizeEstimator
from chunkipy.size_estimators.char_size_estimator import CharSizeEstimator
from chunkipy.size_estimators.word_size_estimator import WordSizeEstimator
from chunkipy.text_splitters import SeparatorTextSplitter


class DashSizeEstimator(BaseSizeEstimator):
    def estimate_size(self, text):
        return len([t for t in text.split("-") if t != '' and t != ' '])


class DashTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator="-")


class SpaceAndDotTextSplitter(SeparatorTextSplitter):
    def __init__(self):
        super().__init__(separator=" .")



class TestTextChunker(unittest.TestCase):

    def test_chunk_short_text_char_estimator(self):
        # when tokens=False (default), it uses CharSizeEstimator by default
        text_chunker = TextChunker(chunk_size=100, size_estimator=CharSizeEstimator())
        text = "This is a short text."
        expected_chunks = ["This is a short text."]
        chunks_text = text_chunker.chunk(text).get_all_text()
        self.assertEqual(chunks_text, expected_chunks)
    
    def test_chunk_short_text_word_estimator(self):
        # when tokens=True, it uses WordSizeEstimator by default
        text_chunker = TextChunker(chunk_size=100)  # using default WordSizeEstimator as size_estimator
        text = "This is a short text."
        expected_chunks = ["This is a short text."]
        chunks_text = text_chunker.chunk(text).get_all_text()
        self.assertEqual(chunks_text, expected_chunks)

    def test_chunk_text_char_estimator(self):
        # when tokens=False, it uses CharSizeEstimator by default
        text_chunker = TextChunker(chunk_size=30, size_estimator=CharSizeEstimator())
        text = "This is a short text. This is another phrase."
        expected_chunks = ["This is a short text. This is ", "another phrase."]
        chunks_text = text_chunker.chunk(text).get_all_text()
        self.assertEqual(chunks_text, expected_chunks)

    def test_chunk_long_text(self):
        text_chunker = TextChunker(chunk_size=105, size_estimator=CharSizeEstimator())
        text = "This is a very long text. " * 16
        expected_chunks = [" ".join(["This is a very long text."] * 4) + " ",
                           " ".join(["This is a very long text."] * 4) + " ",
                           " ".join(["This is a very long text."] * 4) + " ",
                           " ".join(["This is a very long text."] * 4)]
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_chunk_tokenized_short_text(self):
        text_chunker = TextChunker(chunk_size=5)  # using default WordSizeEstimator as size_estimator
        text = "This is a tokenized text."
        expected_chunks = ['This is a tokenized text.']
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_chunk_tokenized_text(self):
        text_chunker = TextChunker(chunk_size=5)
        text = "This is a tokenized text. This is another phrase."
        expected_chunks = ['This is a tokenized text. ',
                           'This is another phrase.']
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_chunk_tokenized_text_custom_split_strategy(self):
        text_splitters = [SpaceAndDotTextSplitter()]
        text_chunker = TextChunker(chunk_size=10, text_splitters=text_splitters)  # using default WordSizeEstimator as size_estimator
        text = "This is a custom split strategy text . The separator is space and dot."
        expected_chunks = ["This is a custom split strategy text .", " The separator is space and dot."]
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_chunk_tokenized_text_custom_tokenizer_and_custom_split_strategy(self):
        text_splitters = [DashTextSplitter()]
        text_chunker = TextChunker(chunk_size=2,
                                   size_estimator=DashSizeEstimator(),
                                   text_splitters=text_splitters)
        text = "This-is-a-custom-tokenized-text."
        expected_chunks = ["This-is-", "a-custom-", "tokenized-text."]
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_overlapping_less_than_max(self):
        # Initialize TextChunker with overlap_ratio
        text_chunker = TextChunker(50, overlap_ratio=0.4)  # using default WordSizeEstimator as size_estimator

        self.assertEqual(text_chunker.overlap_size, 20)

        # Set up test input
        text = "In this unit test, we are evaluating the overlapping functionality. " \
               "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
               "goal is to ensure that overlapping chunks are generated correctly. For this purpose, we have chosen a " \
               "long text that exceeds 100 tokens. By setting the overlap_percent to 0.4, we expect the " \
               "generated chunks to have an overlap of approximately 40%. This will help us verify the effectiveness " \
               "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
               "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
               "for proper overlap. "


        # Assert the overlapping chunks
        expected_chunks = [
            'In this unit test, we are evaluating the overlapping functionality. This is a feature of the TextChunker class, which is important for a proper context keeping. The goal is to ensure that overlapping chunks are generated correctly. For this purpose, ',
            'we have chosen a long text that exceeds 100 tokens. By setting the overlap_percent to 0.4, we expect the generated chunks to have an overlap of approximately 40%. This will help us verify the effectiveness of the overlapping feature. The TextChunker class should be able to handle this scenario and ',
            "help us verify the effectiveness of the overlapping feature. The TextChunker class should be able to handle this scenario and produce the expected results. Let's proceed with running the test and asserting the generated chunks for proper overlap."
        ]
        
        # Generate chunks with overlapping
        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

    def test_overlapping(self):
        # Initialize TextChunker with overlap_ratio = 0.3
        text_chunker = TextChunker(50, overlap_ratio=0.3)  # using default WordSizeEstimator as size_estimator

        self.assertEqual(text_chunker.overlap_size, 15)

        # Set up test input
        text = "In this unit test, we are evaluating the overlapping functionality. " \
               "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
               "goal is to ensure that overlapping chunks are generated correctly. For this purpose, we have chosen a " \
               "long text that exceeds 100 tokens. By setting the overlap_percent to 0.3, we expect the " \
               "generated chunks to have an overlap of approximately 30%. This will help us verify the effectiveness " \
               "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
               "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
               "for proper overlap. "


        # Assert the overlapping chunks
        expected_chunks = [
            'In this unit test, we are evaluating the overlapping functionality. This is a feature of the TextChunker class, which is important for a proper context keeping. The goal is to ensure that overlapping chunks are generated correctly. For this purpose, ',
            'we have chosen a long text that exceeds 100 tokens. By setting the overlap_percent to 0.3, we expect the generated chunks to have an overlap of approximately 30%. This will help us verify the effectiveness of the overlapping feature. The TextChunker class should be able to handle this scenario and ',         
            "of the overlapping feature. The TextChunker class should be able to handle this scenario and produce the expected results. Let's proceed with running the test and asserting the generated chunks for proper overlap."
        ]

        chunks = text_chunker.chunk(text)
        chunks_text = chunks.get_all_text()
        self.assertEqual(expected_chunks, chunks_text)

