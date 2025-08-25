import unittest
from chunkipy.size_estimators.char_size_estimator import CharSizeEstimator
from chunkipy.size_estimators.word_size_estimator import WordSizeEstimator
from chunkipy.text_chunker.fixed_size.fixed_size_text_chunker import FixedSizeTextChunker


class TestFixedSizeTextChunker(unittest.TestCase):
    def test_chunk_short_text(self):
        chunker = FixedSizeTextChunker(chunk_size=20, size_estimator=WordSizeEstimator())
        text = "Short text."
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["Short text."]
        
    def test_chunk_short_text_small_size(self):
        chunker = FixedSizeTextChunker(chunk_size=2, size_estimator=WordSizeEstimator())
        text = "Short text, with some additional content."
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["Short text, ", "with some ", "additional content."]

    def test_chunk_long_text(self):
        chunker = FixedSizeTextChunker(chunk_size=10, size_estimator=CharSizeEstimator())
        text = "abcdefghijABCDEFGHIJ1234567890"
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["abcdefghij", "ABCDEFGHIJ", "1234567890"]

    def test_chunk_with_chunk_size_one(self):
        chunker = FixedSizeTextChunker(chunk_size=1, size_estimator=CharSizeEstimator())
        text = "abc"
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["a", "b", "c"]

    def test_chunk_empty_string(self):
        chunker = FixedSizeTextChunker(chunk_size=5)
        text = ""
        with self.assertRaises(ValueError):
            chunker.chunk(text)

    def test_chunk_size_larger_than_text(self):
        chunker = FixedSizeTextChunker(chunk_size=50)
        text = "tiny"
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["tiny"]

    def test_chunk_with_overlap(self):
        chunker = FixedSizeTextChunker(chunk_size=5, overlap_ratio=0.4, size_estimator=CharSizeEstimator())
        assert chunker.overlap_size == 2
        text = "abcdefghij"
        chunks = chunker.chunk(text).get_all_text()
        assert chunks == ["abcde", "defgh", "ghij"]