from past.builtins import apply

from processes.helpers.get_text_without_punctuation import get_text_without_punctuation
from processes.normalizers.get_text_with_normalized_spaces import get_text_with_normalized_spaces


def has_a_properly_amount_of_words(src: str, tgt: str, min_words=2, max_words=35) -> bool:
    return has_text_properly_amount_of_words(src, min_words, max_words) \
           and has_text_properly_amount_of_words(tgt, min_words, max_words)


def has_text_properly_amount_of_words(text: str, min_words=2, max_words=35) -> bool:
    list_of_cleaning_processes = [
        get_text_without_punctuation,
        get_text_with_normalized_spaces
    ]

    for funct in list_of_cleaning_processes:
        text = apply(funct, text)

    list_of_words = text.split(" ")
    len_list_of_words = len(list_of_words)
    if len_list_of_words > max_words or len_list_of_words < min_words:
        return False
    return True
