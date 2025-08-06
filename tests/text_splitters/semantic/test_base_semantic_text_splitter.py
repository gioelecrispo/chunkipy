import unittest
from typing import List
from chunkipy.text_splitters.semantic.base_semantic_text_splitter import BaseSemanticTextSplitter

class DummySemanticTextSplitter(BaseSemanticTextSplitter):
    # Simple implementation: split by whitespace
    def _split(self, text: str) -> List[str]:
        return text.split()

class TestBaseSemanticTextSplitter(unittest.TestCase):
    def setUp(self):
        self.splitter = DummySemanticTextSplitter(text_limit=10)

    def test_split_basic(self):
        text = "This is a test"
        result = self.splitter.split(text)
        self.assertEqual(result, ["This", "is", "a", "test"])

    def test_split_empty_string(self):
        text = ""
        with self.assertRaises(ValueError):
            self.splitter.split(text)

    def test_split_with_large_text(self):
        text = "word " * 50  # 250 chars, text_limit=10, so text is divided into multiple parts (to control input size for semantic models)
        result = self.splitter.split(text.strip())
        self.assertTrue(all(isinstance(x, str) for x in result))
        self.assertEqual(len(result), 50)

    def test_split_preserves_semantics(self):
        text = "one two three four five six seven eight nine ten eleven"
        result = self.splitter.split(text)
        self.assertIn("eleven", result)
        self.assertEqual(result[0], "one")

    def test_split_with_custom_text_limit(self):
        splitter = DummySemanticTextSplitter(text_limit=5)
        text = "a b c d e f g"
        result = splitter.split(text)
        self.assertEqual(result, ["a", "b", "c", "d", "e", "f", "g"])

    def test_split_raises_on_non_string(self):
        with self.assertRaises(TypeError):
            self.splitter.split(12345)

    def test_split_with_long_word(self):
        text = "a " + "x" * 100 + " b"
        result = self.splitter.split(text)
        self.assertIn("b", result)
        self.assertIn("a", result)
        self.assertIn("x" * 100, result)
