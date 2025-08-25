from chunkipy.size_estimators import WordSizeEstimator
from chunkipy import RecursiveTextChunker


if __name__ == "__main__":

    with open("examples/texts/napoleon.txt", "r") as file:
        text = file.read()
        
    try:
        from chunkipy.text_splitters.semantic.sentences import SpacySentenceTextSplitter
        from chunkipy.size_estimators.openai_size_estimator import OpenAISizeEstimator

        word_size_estimator = WordSizeEstimator()
        openai_size_estimator = OpenAISizeEstimator()

        print(f"Num of chars: {len(text)}")
        print(f"Num of tokens (using WordSizeEstimator): {word_size_estimator.estimate_size(text)}")
        print(f"Num of tokens (using OpenAISizeEstimator): {openai_size_estimator.estimate_size(text)}")

        spacy_text_splitter = SpacySentenceTextSplitter()

        models_map={
            "en": "en_core_web_sm",
            "de": "de_core_news_sm",
            "it": "it_core_news_sm",
        }

        text_chunker = RecursiveTextChunker(
            chunk_size=200,
            overlap_ratio=0.25,
            size_estimator=openai_size_estimator,
            text_splitters=[spacy_text_splitter]
        )

        chunks = text_chunker.chunk(text)
        print(f"Got: {len(chunks)}")
        print(f"Here the text_parts: {chunks.get_all_text_parts()}")
    except MissingDependencyError as e:
        print(f"Error: {e}")

    


