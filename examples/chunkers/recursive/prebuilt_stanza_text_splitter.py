from chunkipy import RecursiveTextChunker
from chunkipy.utils import MissingDependencyError


if __name__ == "__main__":

    with open("examples/texts/napoleon.txt", "r") as file:
        text = file.read()

    try:
        from chunkipy.text_splitters.semantic.sentences import StanzaSentenceTextSplitter
        
        stanza_text_splitter = StanzaSentenceTextSplitter()
        
        text_chunker = RecursiveTextChunker(
            chunk_size=200,
            overlap_ratio=0.25,
            text_splitters=[stanza_text_splitter]
        )

        chunks = text_chunker.chunk(text)
        print(f"Got: {len(chunks)}")
        print(f"Here the text_parts: {chunks.get_all_text_parts()}")
    except MissingDependencyError as e:
        print(f"Error: {e}")

    


