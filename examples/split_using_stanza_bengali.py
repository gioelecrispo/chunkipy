from chunkipy import TextChunker
from chunkipy.text_splitters.semantic.sentences import StanzaSentenceTextSplitter


if __name__ == "__main__":

    # Note: The text in "bengali.txt" is in Bengali language.
    with open("examples/texts/bengali.txt", "r") as file:
        text = file.read()

    stanza_text_splitter = StanzaSentenceTextSplitter()

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        text_splitters=[stanza_text_splitter]
    )

    # The StanzaSentenceTextSplitter will raise an error because Bengali is not supported by Stanza.
    try:
        # Attempt to chunk the text
        chunks = text_chunker.chunk(text)
    except ValueError as e:
        # Handle the case where the language is not supported by Stanza
        print(f"Error: {e}")



