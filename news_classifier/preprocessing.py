"""News text normalization and optional Korean morphological tokenization."""
import html
import re
import unicodedata
from functools import lru_cache


def _text(value):
    if not isinstance(value, str):
        raise TypeError("News text must be a string")
    value = unicodedata.normalize("NFKC", html.unescape(value))
    value = re.sub(r"<[^>]*>", " ", value)
    value = re.sub(r"(?:https?|ftp)://\S+|\S+@\S+", " ", value)
    return " ".join(value.split())


def _translate_hanja(value):
    if any("\u4e00" <= c <= "\u9fff" for c in value):
        import hanja
        return hanja.translate(value, "substitution")
    return value


def preprocess_sent(sentence):
    """Normalize markup, mask digits, and keep words for tokenization."""
    value = _translate_hanja(_text(sentence))
    value = re.sub(r"\d+", " NUM ", value)
    return " ".join(re.findall(r"[가-힣A-Za-z]+", value))


def cleaning_strings(input_text):
    """Normalize text while retaining separate punctuation tokens."""
    value = re.sub(r"\d+", "NUM", _translate_hanja(_text(input_text)))
    return " ".join(re.findall(r"\w+|[^\w\s]", value))


@lru_cache(maxsize=1)
def _mecab():
    from konlpy.tag import Mecab
    return Mecab()


def glove_tokenizer(text):
    return [f"{word.strip()}/{tag.strip()}" for word, tag in _mecab().pos(text)
            if word.strip()]
