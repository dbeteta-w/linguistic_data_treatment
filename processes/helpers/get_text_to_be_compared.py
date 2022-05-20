import re

from past.builtins import apply

from processes.helpers.get_text_without_punctuation import get_text_without_punctuation


def get_text_to_be_compared(text: str) -> str:
    list_of_cleaning_processes = [
        get_text_without_punctuation,
        lambda x: x.casefold(),
        lambda x: re.sub(r"\s", "", x),
    ]

    for funct in list_of_cleaning_processes:
        text = apply(funct, text)

    return text
