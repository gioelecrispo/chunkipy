import os
from openai import OpenAI
from chunkipy.size_estimators import openai_size_estimator
from chunkipy.text_chunker import text_chunker
from chunkipy.text_splitters.semantic.llm.openai_text_splitter import OpenAITextSplitter
from chunkipy import TextChunker
from chunkipy.size_estimators.openai_size_estimator import OpenAISizeEstimator

if __name__ == "__main__":
    with open("examples/texts/napoleon.txt", "r") as file:
        text = file.read()

    openai_size_estimator = OpenAISizeEstimator()

    openai_text_splitter = OpenAITextSplitter(
        model=OpenAI(
            api_key=os.getenv("OPENAI_ΑΡΙΚΕΥ"),
            max_retries=2,
        )
    )

    deployment_model_name=os.getenv("OPENAI_DEPLOYMENT_MODEL_NAME")
    
    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0,
        tokens=True,
        size_estimator=openai_size_estimator,
        text_splitters=[openai_text_splitter]
    )

    chunks = text_chunker.chunk(text)
    print(f"Got: {len(chunks)}")
    print (f"Here the text_parts: {chunks.get_all_text_parts()}")
