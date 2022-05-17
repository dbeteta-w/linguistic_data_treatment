import re

from helpers.remove_punctuation import remove_punctuation


def clean_to_be_compared(text: str):
    text = remove_punctuation(text)
    return re.sub(r"\s", "", text).casefold()