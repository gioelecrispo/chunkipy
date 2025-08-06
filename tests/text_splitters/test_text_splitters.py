import unittest
from chunkipy.text_splitters import SemicolonTextSplitter, CommaTextSplitter, WordTextSplitter, NewlineTextSplitter, FullStopTextSplitter


class TestTextSplitter(unittest.TestCase):
    def test_split_text_by_delimiter(self):
        splitter = WordTextSplitter()
        text = "This is a test"
        result = splitter.split(text)
        assert result == ["This ", "is ", "a ", "test"]

    def test_split_text_by_newline(self):
        splitter = NewlineTextSplitter()
        text = "Line1\nLine2\nLine3"
        result = splitter.split(text)
        assert result == ["Line1\n", "Line2\n", "Line3"]

    def test_split_text_empty_string(self):
        splitter = WordTextSplitter()
        text = ""
        with self.assertRaises(ValueError):
            splitter.split(text)
            self.fail("Expected ValueError not raised.")

    def test_split_text_no_delimiter_in_text(self):
        splitter = CommaTextSplitter()
        text = "NoDelimiterHere"
        result = splitter.split(text)
        assert result == ["NoDelimiterHere"]

    def test_split_text_multiple_delimiters(self):
        splitter = CommaTextSplitter()
        text = "word1, word2, word3, , word4"
        result = splitter.split(text)
        assert result == ["word1, ", "word2, ", "word3, ", "word4"]

    def test_split_text_with_strip(self):
        splitter = CommaTextSplitter()
        text = " a , b , c "
        result = splitter.split(text)
        assert result == [" a , ", "b , ", "c "]
        
    def test_word_split_text_space_at_the_beginning(self):
        splitter = WordTextSplitter()
        text = "                    word1,word2,word3,word4,word5"
        result = splitter.split(text)
        assert result == ["word1,word2,word3,word4,word5"]
        
    def test_fullstop_split_text_space_at_the_beginning(self):
        splitter = FullStopTextSplitter()
        text = "                    word1,word2,word3,word4,word5"
        result = splitter.split(text)
        assert result == ["                    word1,word2,word3,word4,word5"]
        


