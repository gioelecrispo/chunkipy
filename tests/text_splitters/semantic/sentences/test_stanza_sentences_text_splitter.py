import unittest
from unittest.mock import MagicMock
from chunkipy.text_splitters.semantic.sentences.stanza_sentence_text_splitter import StanzaSentenceTextSplitter


class FakeStanzaSentenceTextSplitter(StanzaSentenceTextSplitter):
    def __init__(self, *args, stanza_components=None, **kwargs):
        self._test_stanza_components = stanza_components
        super().__init__(*args, **kwargs)

    def _get_stanza_components(self):
        return self._test_stanza_components


class TestStanzaSentenceTextSplitter(unittest.TestCase):
    def setUp(self):
        # Shared fakes injected via constructor — no monkey patching needed
        self.mock_langdetect = MagicMock()
        self.mock_download_method = MagicMock()
        self.mock_download_method.REUSE_RESOURCES = "reuse"
        self.mock_pipeline_cls = MagicMock()

        self.splitter = FakeStanzaSentenceTextSplitter(
            language_detector=self.mock_langdetect,
            stanza_components=(self.mock_download_method, self.mock_pipeline_cls),
        )

    def test_split_english_text(self):
        mock_sentence1 = MagicMock()
        mock_sentence1.text = "Hello world."
        mock_sentence2 = MagicMock()
        mock_sentence2.text = "How are you?"
        mock_pipeline_instance = MagicMock()
        mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
        self.mock_pipeline_cls.return_value = mock_pipeline_instance

        self.mock_langdetect.detect.return_value = "en"

        text = "Hello world. How are you?"
        result = self.splitter._split(text)

        self.assertEqual(result, ["Hello world. ", "How are you? "])
        self.mock_langdetect.detect.assert_called_once_with(text)
        self.mock_pipeline_cls.assert_called_once_with(
            lang="en", processors="tokenize", download_method="reuse"
        )
        mock_pipeline_instance.assert_called_once_with(text)

    def test_split_non_english_text(self):
        mock_sentence1 = MagicMock()
        mock_sentence1.text = "Ciao mondo."
        mock_sentence2 = MagicMock()
        mock_sentence2.text = "Come stai?"
        mock_pipeline_instance = MagicMock()
        mock_pipeline_instance.return_value.sentences = [mock_sentence1, mock_sentence2]
        self.mock_pipeline_cls.return_value = mock_pipeline_instance

        self.mock_langdetect.detect.return_value = "it"

        text = "Ciao mondo. Come stai?"
        result = self.splitter._split(text)

        self.assertEqual(result, ["Ciao mondo. ", "Come stai? "])
        self.mock_langdetect.detect.assert_called_once_with(text)
        self.mock_pipeline_cls.assert_called_once_with(
            lang="it", processors="tokenize", download_method="reuse"
        )
        mock_pipeline_instance.assert_called_once_with(text)

    def test_split_empty_text(self):
        mock_pipeline_instance = MagicMock()
        mock_pipeline_instance.return_value.sentences = []
        self.mock_pipeline_cls.return_value = mock_pipeline_instance

        self.mock_langdetect.detect.return_value = "en"

        result = self.splitter._split("")
        self.assertEqual(result, [])




