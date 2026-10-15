# Changes

- Grouped training, models, and data adapters into `news_classifier`.
- Replaced historical notebook-derived preprocessing with a Unicode/HTML normalizer and lazy optional Hanja/Mecab adapters. Tokenization is not byte-identical to historical preprocessing.
- Replaced the copied dataframe adapter with wrappers around torchtext's `Example.fromlist` and `Dataset` constructors.
- Retained the model implementation and training interface; full training remains untested.
