Overview
===============

.. sidebar:: Splitter classes

   - :class:`BaseTextSplitter <chunkipy.text_splitters.BaseTextSplitter>`
   - :class:`WordTextSplitter <chunkipy.text_splitters.WordTextSplitter>`
   - :class:`FullStopTextSplitter <chunkipy.text_splitters.FullStopTextSplitter>`
   - :class:`NewlineTextSplitter <chunkipy.text_splitters.NewlineTextSplitter>`
   - :class:`CommaTextSplitter <chunkipy.text_splitters.CommaTextSplitter>`
   - :class:`SemicolonTextSplitter <chunkipy.text_splitters.SemicolonTextSplitter>`
   - :class:`ColonTextSplitter <chunkipy.text_splitters.ColonTextSplitter>`
   - :class:`SpacySentenceTextSplitter <chunkipy.text_splitters.semantic.sentences.SpacySentenceTextSplitter>`
   - :class:`StanzaSentenceTextSplitter <chunkipy.text_splitters.semantic.sentences.StanzaSentenceTextSplitter>`

Text splitters define how input text is divided before chunk composition.

Every splitter follows a shared interface, so you can replace built-in
strategies with custom implementations without changing your chunker API.



Built-in basic splitters
-------------------------

Chunkipy includes delimiter-based splitters in ``chunkipy.text_splitters``:

- :class:`WordTextSplitter <chunkipy.text_splitters.WordTextSplitter>`
- :class:`FullStopTextSplitter <chunkipy.text_splitters.FullStopTextSplitter>`
- :class:`NewlineTextSplitter <chunkipy.text_splitters.NewlineTextSplitter>`
- :class:`CommaTextSplitter <chunkipy.text_splitters.CommaTextSplitter>`
- :class:`SemicolonTextSplitter <chunkipy.text_splitters.SemicolonTextSplitter>`
- :class:`ColonTextSplitter <chunkipy.text_splitters.ColonTextSplitter>`

Semantic sentence splitters
----------------------------

For NLP-aware sentence segmentation, use:

- :class:`SpacySentenceTextSplitter <chunkipy.text_splitters.semantic.sentences.SpacySentenceTextSplitter>`
- :class:`StanzaSentenceTextSplitter <chunkipy.text_splitters.semantic.sentences.StanzaSentenceTextSplitter>`


When to use what
-----------------

- Use basic splitters for lightweight, deterministic splitting.
- Use spaCy splitter when your project already uses spaCy pipelines.
- Use Stanza splitter when Stanza language coverage fits your workflow.
- Implement a custom splitter by extending :class:`BaseTextSplitter <chunkipy.text_splitters.BaseTextSplitter>` when your domain needs specific rules.