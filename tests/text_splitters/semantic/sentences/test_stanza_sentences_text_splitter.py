import unittest
from unittest.mock import patch, MagicMock
from chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter import StanzaSentenceTextSplitter

class TestStanzaSentenceTextSplitter(unittest.TestCase):
    def setUp(self):
        self.splitter = StanzaSentenceTextSplitter()

    def test_split_english_text(self):
        with patch("langdetect.detect") as mock_detect, \
             patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:

            mock_detect.return_value = "en"
            mock_download_method = MagicMock()
            mock_download_method.REUSE_RESOURCES = "reuse"
            mock_pipeline_cls = MagicMock()
            mock_sentence1 = MagicMock()
            mock_sentence1.text = "Hello world."
            mock_sentence2 = MagicMock()
            mock_sentence2.text = "How are you?"
            mock_pipeline_instance = MagicMock()
            # The pipeline is called with the text, so set .sentences on the result of that call
            mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
            mock_pipeline_cls.return_value = mock_pipeline_instance

            mock_import_deps.return_value = (None, mock_download_method, mock_pipeline_cls)

            text = "Hello world. How are you?"
            result = self.splitter._split(text)
            self.assertEqual(result, ["Hello world. ", "How are you? "])
            mock_detect.assert_called_once_with(text)
            mock_pipeline_cls.assert_called_once_with(
                lang="en", processors="tokenize", download_method="reuse"
            )
            mock_pipeline_instance.assert_called_once_with(text)


    def test_split_non_english_text(self):
        with patch("langdetect.detect") as mock_detect, \
             patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:

            mock_detect.return_value = "it"
            mock_download_method = MagicMock()
            mock_download_method.REUSE_RESOURCES = "reuse"
            mock_pipeline_cls = MagicMock()
            mock_sentence1 = MagicMock()
            mock_sentence1.text = "Ciao mondo."
            mock_sentence2 = MagicMock()
            mock_sentence2.text = "Come stai?"
            mock_pipeline_instance = MagicMock()
            # The pipeline is called with the text, so set .sentences on the result of that call
            mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
            mock_pipeline_cls.return_value = mock_pipeline_instance

            mock_import_deps.return_value = (None, mock_download_method, mock_pipeline_cls)

            text = "Ciao mondo. Come stai?"
            result = self.splitter._split(text)
            self.assertEqual(result, ["Ciao mondo. ", "Come stai? "])
            mock_detect.assert_called_once_with(text)
            mock_pipeline_cls.assert_called_once_with(
                lang="it", processors="tokenize", download_method="reuse"
            )


    def test_split_empty_text(self):
        with patch("langdetect.detect") as mock_detect, \
             patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:
            mock_detect.return_value = "en"
            mock_download_method = MagicMock()
            mock_download_method.REUSE_RESOURCES = "reuse"
            mock_pipeline_cls = MagicMock()
            mock_pipeline_instance = MagicMock()
            mock_pipeline_instance.return_value.sentences = []
            mock_pipeline_cls.return_value = mock_pipeline_instance.return_value
            mock_import_deps.return_value = (None, mock_download_method, mock_pipeline_cls)

            text = ""
            result = self.splitter._split(text)
            self.assertEqual(result, [])
