Overview
===============

.. sidebar:: Size estimator classes

   - :class:`BaseSizeEstimator <chunkipy.size_estimators.BaseSizeEstimator>`
   - :class:`CharSizeEstimator <chunkipy.size_estimators.CharSizeEstimator>`
   - :class:`WordSizeEstimator <chunkipy.size_estimators.WordSizeEstimator>`
   - :class:`OpenAISizeEstimator <chunkipy.size_estimators.OpenAISizeEstimator>`

Size estimators define *how* chunk size is measured. The selected estimator
directly affects chunk boundaries, overlap behavior, and final chunk count.

Choose the estimator according to your downstream workload:

- use character-based sizing for deterministic low-level control;
- use word-based sizing for general NLP tasks;
- use token-based sizing when your target model enforces token limits.

If built-in strategies are not enough, you can implement your own estimator by
extending :class:`BaseSizeEstimator <chunkipy.size_estimators.BaseSizeEstimator>`
to adapt chunk sizing to any domain-specific requirement.


Built-in estimators
-------------------

Chunkipy currently provides three estimators:

- :class:`CharSizeEstimator <chunkipy.size_estimators.CharSizeEstimator>`
- :class:`WordSizeEstimator <chunkipy.size_estimators.WordSizeEstimator>`
- :class:`OpenAISizeEstimator <chunkipy.size_estimators.OpenAISizeEstimator>`


Quick comparison
----------------

.. list-table::
   :header-rows: 1
   :widths: 24 26 18 32

   * - Estimator
     - Unit
     - Extra dependency
     - Recommended when
   * - ``CharSizeEstimator``
     - Characters
     - None
     - You need deterministic and very fast sizing
   * - ``WordSizeEstimator``
     - Words
     - None
     - You want human-readable chunk lengths for generic NLP
   * - ``OpenAISizeEstimator``
     - Tokens (``tiktoken``)
     - ``chunkipy[tiktoken]``
     - You need chunk sizes aligned with LLM token budgets


Choosing an estimator
---------------------

- Start with :class:`WordSizeEstimator <chunkipy.size_estimators.WordSizeEstimator>` for most projects.
- Prefer :class:`OpenAISizeEstimator <chunkipy.size_estimators.OpenAISizeEstimator>` for prompt budgeting and LLM/RAG pipelines.
- Switch to :class:`CharSizeEstimator <chunkipy.size_estimators.CharSizeEstimator>` when you need strict, tokenizer-independent reproducibility.
- Build a custom estimator by subclassing :class:`BaseSizeEstimator <chunkipy.size_estimators.BaseSizeEstimator>` when your sizing logic is domain-specific.

For implementation details and usage examples, see the dedicated pages:

- :doc:`char`
- :doc:`word`
- :doc:`openai`