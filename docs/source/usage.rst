Usage
==============
In this section, we will explore how to use Chunkipy effectively, including its basic and advanced features.
To use Chunkipy, you first need to install it. You can do this using pip, as described in the installation guide. 
Once installed, you can start using it to chunk text.


Chunk Size and Token Counting
-----------------------------
Chunkipy allows you to specify the chunk size in either characters or tokens.
By default, it counts characters, but you can set it to count tokens instead. This flexibility is particularly useful for applications that require token-based processing, such as working with language models like OpenAI's GPT.
You can easily switch between character and token counting by setting the ``tokens`` parameter when creating a
``TextChunker`` instance.
``tokens = False`` by default, so it will count characters. If you want to count tokens, set it to True.

Here is an example of how to create a ``TextChunker`` instance with character counting:

.. code-block:: python

    from chunkipy import TextChunker

    text_chunker = TextChunker(100, tokens=False)
    text = "This is a sample text that will be chunked into smaller pieces."
    chunks = text_chunker.chunk(text)
    print(chunks)

And here is an example of how to create a ``TextChunker`` instance with token counting:

.. code-block:: python

    from chunkipy import TextChunker

    text_chunker = TextChunker(100, tokens=True)
    text = "This is a sample text that will be chunked into smaller pieces."
    chunks = text_chunker.chunk(text)
    print(chunks)



Overlapping
--------------------------
Chunkipy also supports overlapping chunks, which can be useful for preserving context across chunks.
You can define an ``overlap_percentage`` to create overlapping chunks, ensuring that important context is
not lost when splitting the text.

Here is an example of how to create overlapping chunks:

.. code-block:: python

    from chunkipy import TextChunker

    if __name__ == "__main__":
        # Set up test input
        text = "In this example test, we are evaluating the overlapping functionality. " \
            "This is a feature of the TextChunker class, which is important for a proper context keeping. The " \
            "goal is: 1. to ensure that chunks are generated correctly, 2. check the overlapping. For this purpose, we have chosen a " \
            "long text that exceeds 100 tokens. By setting the overlap_percent to 0.3, we expect the " \
            "generated chunks to have an overlap of approximately 30%. This will help us verify the effectiveness " \
            "of the overlapping feature. The TextChunker class should be able to handle this scenario and " \
            "produce the expected results. Let's proceed with running the test and asserting the generated chunks " \
            "for proper overlap. "

        # Generate chunks with overlapping
        text_chunker = TextChunker(50, tokens=True, overlap_ratio=0.3)  # using WordSizeEstimator by default
        chunks = text_chunker.chunk(text)

        # Print the resulting chunks
        for i, chunk in enumerate (chunks):
            print(f"Chunk {i + 1}: {chunk}")


Text Splitters
---------------

Chunkipy provides several built-in text splitters that you can use to customize the chunking process. 
These splitters can help you define how the text should be divided into smaller parts based on specific criteria, such as sentence boundaries or custom delimiters.
You can also create your own custom text splitter if the built-in ones do not meet your needs.


Prebuilt Basic Text Splitters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Chunkipy includes several prebuilt text splitters that can be used to split text into chunks based on different criteria.
For example, you can use the ``WordTextSplitter`` to split text into chunks based on word boundaries, or the ``CharacterTextSplitter`` to split text into chunks based on character count.
Here is an example of how to use the ``WordTextSplitter``:

.. code-block:: python

    from chunkipy import TextChunker
    from chunkipy.text_splitters import WordTextSplitter

    word_text_splitter = WordTextSplitter()

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        tokens=True,
        text_splitters=[word_text_splitter]
    )

    text = "This is a sample text that will be split into chunks based on word boundaries."
    chunks = text_chunker.chunk(text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")


Prebuilt Sentence Text Splitters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also use Chunkipy with different splitters and estimators. 
For example, you can use the Stanza or SpaCy splitters to handle more complex text structures.
Remember to install the optional dependencies, i.e. ``pip install chunkipy[stanza-splitter]`` or ``pip install chunkipy[spacy-splitter]``, if you want to use these features.

.. code-block:: python
    from chunkipy import TextChunker
    from chunkipy.text_splitters.semantic.sentences import StanzaSentenceTextSplitter
    
    stanza_text_splitter = StanzaSentenceTextSplitter()

    text_chunker = TextChunker(
        chunk_size=200,
        overlap_ratio=0.25,
        tokens=True,
        text_splitters=[stanza_text_splitter]
    )

    text = "This is a sample text that will be split into chunks based on sentence boundaries."
    chunks = text_chunker.chunk(text)   

In the example above, we use the prebuilt ``StanzaSentenceTextSplitter`` to split the text into chunks based on sentence boundaries.
You can also use the ``SpacySentenceTextSplitter`` in a similar way. There is a script called ``split_using_spacy.py`` in the ``examples`` directory of the chunkipy repository that demonstrates how to use SpaCy.

Custom Text Splitters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the built-in splitters do not meet your needs, you can create your own custom text splitter by implementing the ``TextSplitter`` interface.
This gives you full control over how the text is split into chunks, enabling you to create highly specialized chunking behavior tailored to your specific needs.


Here is an example of how to create a custom text splitter:

.. code-block:: python

    from chunkipy import TextChunker
    from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter

    text = "This is a small text -> with custom split strategy."

    class ArrowTextSplitter(BaseTextSplitter):
        def split(self, text):
            return [t for t in text.split("->") if t != '' and t != ' ']

    # Create a TextChunker object with custom text splitter (using WordSizeEstimator by default)
    arrow_text_splitter = ArrowTextSplitter()
    text_chunker = TextChunker(chunk_size=8, tokens=True, text_splitters=[arrow_text_splitter])
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")

This example demonstrates how to create a custom text splitter that splits the text based on a specific delimiter (``->`` in this case). You can modify the `split` method to implement any custom logic you need for splitting the text.


Custom Size Estimators
--------------------------
Chunkipy also allows you to define your own custom size estimators by implementing the ``BaseSizeEstimator`` interface.
This gives you the flexibility to create size estimators that suit your specific requirements, such as estimating the size of text based on custom criteria or using different tokenization methods.
Here is an example of how to create a custom size estimator:

.. code-block:: python

    from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator

    class HalfLengthSizeEstimator(BaseSizeEstimator):
        def estimate_size(self, text):
            # Implement your custom size estimation logic here
            return int(len(text)/2)  # Example: return half the length of the text as the size

    # Create an instance of the custom size estimator
    half_length_size_estimator = HalfLengthSizeEstimator()

    # Use the custom size estimator in a TextChunker
    text_chunker = TextChunker(chunk_size=100, tokens=True, size_estimator=half_length_size_estimator)
    text = "This is a sample text that will be chunked using a custom size estimator."
    chunks = text_chunker.chunk(text)

    # Print the resulting chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")


Examples
-----------------
You can find more examples in the ``examples`` directory of the chunkipy repository.

