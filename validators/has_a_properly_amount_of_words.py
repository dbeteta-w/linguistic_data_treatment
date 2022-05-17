import re

from helpers.remove_punctuation import remove_punctuation


def has_a_properly_amount_of_words(src: str, tgt: str, min_words=2, max_words=35):
    return _has_a_properly_amount_of_words(src, min_words, max_words) \
           and _has_a_properly_amount_of_words(tgt, min_words, max_words)


def _has_a_properly_amount_of_words(text: str, min_words=2, max_words=35):
    text = remove_punctuation(text)
    text_with_normalized_spaces = re.sub(r"[ ]{2,}", " ", text).strip()
    list_of_words = text_with_normalized_spaces.split(" ")
    if len(list_of_words) > max_words or len(list_of_words) < min_words:
        return False
    return True
