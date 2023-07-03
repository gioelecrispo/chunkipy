import stanza
from stanza import DownloadMethod
import langdetect
import logging


logging.getLogger('stanza').disabled = True


def split_by_sentences(text):
    lang = langdetect.detect(text)
    sentence_tokenizer = stanza.Pipeline(lang=lang, processors='tokenize', download_method=DownloadMethod.REUSE_RESOURCES)
    return [s.text + " " for s in sentence_tokenizer(text).sentences]


def split_by_separator(text: str, sep: str):
    text = text.split(sep)
    text_pieces = [t + sep for t in text if t != '' and ' ']
    text_pieces[-1] = text_pieces[-1][:-len(sep)]
    return text_pieces


def split_by_semicolon(text: str):
    return split_by_separator(text, '; ')


def split_by_colon(text: str):
    return split_by_separator(text, ': ')


def split_by_comma(text: str):
    return split_by_separator(text, ', ')


def split_by_word(text: str):
    return split_by_separator(text, ' ')
