from chunkipy import TextChunker
from chunkipy.size_estimators import WordSizeEstimator
from chunkipy.text_splitters.semantic.sentences import SpacyTextSentenceSplitter
from chunkipy.size_estimators.openai_size_estimator import OpenAISizeEstimator

if __name__ == "__main__":

    with open("texts/napoleon.txt", "r") as file:
        text = file.read()

    word_size_estimator = WordSizeEstimator()
    openai_size_estimator = OpenAISizeEstimator()

    print(f"Num of chars: {len(text)}")
    print(f"Num of tokens (using WordSizeEstimator): {word_size_estimator.estimate_size(text)}")
    print(f"Num of tokens (using OpenAISizeEstimator): {openai_size_estimator.estimate_size(text)}")

    spacy_text_splitter = SpacyTextSentenceSplitter()

    models_map={
        "en": "en_core_web_sm",
        "de": "de_core_news_sm",
        "it": "it_core_news_sm",
    }

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        tokens=True,
        size_estimator=openai_size_estimator,
        text_splitters=[spacy_text_splitter]
    )

    chunks = text_chunker.chunk(text)
    print(f"Got: {len(chunks)}")
    print(f"Here the text_parts: {chunks.get_all_text_parts()}")


