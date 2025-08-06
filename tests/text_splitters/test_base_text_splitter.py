import unittest
from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter

class DummyTextSplitter(BaseTextSplitter):
    def _split(self, text: str) -> list[str]:
        # Simple splitter for testing: split by spaces
        return text.split()

class TestBaseTextSplitter(unittest.TestCase):
    def test_split_valid_text(self):
        splitter = DummyTextSplitter()
        text = "Hello world from chunkipy"
        result = splitter.split(text)
        self.assertEqual(result, ["Hello", "world", "from", "chunkipy"])

    def test_split_invalid_type_raises(self):
        splitter = DummyTextSplitter()
        for invalid_text in [None, 123, 12.5, [], {}, object()]:
            with self.assertRaisesRegex(TypeError, "Text must be a non-empty string"):
                splitter.split(invalid_text)

    def test_split_empty_or_whitespace_raises(self):
        splitter = DummyTextSplitter()
        for empty_text in ["", "   ", "\n\t"]:
            with self.assertRaisesRegex(ValueError, "Text cannot be empty or whitespace only"):
                splitter.split(empty_text)

    def test_base_text_splitter_split_not_implemented(self):
        class IncompleteSplitter(BaseTextSplitter):
            pass
        with self.assertRaises(TypeError):
            IncompleteSplitter()

    def test_base_text_splitter_split_method_raises_not_implemented(self):
        class NotImplementedSplitter(BaseTextSplitter):
            def _split(self, text: str) -> list[str]:
                return super()._split(text)
        splitter = NotImplementedSplitter()
        with self.assertRaisesRegex(NotImplementedError, "Subclasses must implement the split method"):
            splitter.split("some text")
