from chunkipy import TextChunker
from chunkipy.text_splitters.semantic.sentences import StanzaSentenceTextSplitter


if __name__ == "__main__":

    with open("examples/texts/napoleon.txt", "r") as file:
        text = file.read()

    stanza_text_splitter = StanzaSentenceTextSplitter()

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        text_splitters=[stanza_text_splitter]
    )

    chunks = text_chunker.chunk(text)
    print(f"Got: {len(chunks)}")
    print(f"Here the text_parts: {chunks.get_all_text_parts()}")


