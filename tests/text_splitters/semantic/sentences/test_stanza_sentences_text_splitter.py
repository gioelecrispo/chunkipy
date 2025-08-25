import unittest
from unittest.mock import patch, MagicMock
from chunkipy.text_splitters.semantic.sentences.stanza_sentence_text_splitter import StanzaSentenceTextSplitter

            
class TestStanzaSentenceTextSplitter(unittest.TestCase):
    def setUp(self):
        self.splitter = StanzaSentenceTextSplitter()
        
        # Shared Mocks
        self.mock_langdetect = MagicMock()
        self.mock_download_method = MagicMock()
        self.mock_download_method.REUSE_RESOURCES = "reuse"
        self.mock_pipeline_cls = MagicMock()
        self.mock_pipeline_instance = MagicMock()
        self.mock_pipeline_cls.return_value = self.mock_pipeline_instance

        # Side effect for import_dependencies
        self.import_deps_side_effect = lambda *args, **kwargs: (
            self.mock_langdetect if kwargs.get("package_name") == "langdetect"
            else (None, self.mock_download_method, self.mock_pipeline_cls)
        )

    def test_split_english_text(self):
        with patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:
          
            mock_import_deps.side_effect = self.import_deps_side_effect
            
            self.mock_langdetect.detect.return_value = "en"
            mock_sentence1 = MagicMock()
            mock_sentence1.text = "Hello world."
            mock_sentence2 = MagicMock()
            mock_sentence2.text = "How are you?"
            self.mock_pipeline_instance = MagicMock()
            # The pipeline is called with the text, so set .sentences on the result of that call
            self.mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
            self.mock_pipeline_cls.return_value = self.mock_pipeline_instance

            text = "Hello world. How are you?"
            result = self.splitter._split(text)
            self.assertEqual(result, ["Hello world. ", "How are you? "])
            self.mock_langdetect.detect.assert_called_once_with(text)
            self.mock_pipeline_cls.assert_called_once_with(
                lang="en", processors="tokenize", download_method="reuse"
            )
            self.mock_pipeline_instance.assert_called_once_with(text)


    def test_split_non_english_text(self):
        with patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:
            mock_import_deps.side_effect = self.import_deps_side_effect
            
            self.mock_langdetect.detect.return_value = "it"
            mock_sentence1 = MagicMock()
            mock_sentence1.text = "Ciao mondo."
            mock_sentence2 = MagicMock()
            mock_sentence2.text = "Come stai?"
            self.mock_pipeline_instance = MagicMock()
            # The pipeline is called with the text, so set .sentences on the result of that call
            self.mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
            self.mock_pipeline_cls.return_value = self.mock_pipeline_instance

            text = "Ciao mondo. Come stai?"
            result = self.splitter._split(text)
            self.assertEqual(result, ["Ciao mondo. ", "Come stai? "])
            self.mock_langdetect.detect.assert_called_once_with(text)
            self.mock_pipeline_cls.assert_called_once_with(
                lang="it", processors="tokenize", download_method="reuse"
            )


    def test_split_empty_text(self):
        with patch("chunkipy.text_splitters.semantic.sentences.stanza_sentences_text_splitter.import_dependencies") as mock_import_deps:
            mock_import_deps.side_effect = self.import_deps_side_effect
            
            self.mock_langdetect.detect.return_value = "en"

            self.mock_pipeline_instance.return_value.sentences = []
            self.mock_pipeline_cls.return_value = self.mock_pipeline_instance.return_value
            mock_import_deps.return_value = (None, self.mock_download_method, self.mock_pipeline_cls)

            text = ""
            result = self.splitter._split(text)
            self.assertEqual(result, [])




