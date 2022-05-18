import re

from past.builtins import apply

from helpers.remove_punctuation import remove_punctuation


def clean_to_be_compared(text: str) -> str:
    list_of_cleaning_processes = [
        remove_punctuation,
        lambda x: x.casefold(),
        lambda x: re.sub(r"\s", "", x),
    ]

    for funct in list_of_cleaning_processes:
        text = apply(funct, text)

    return text
