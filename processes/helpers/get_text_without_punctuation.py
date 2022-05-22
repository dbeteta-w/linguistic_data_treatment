import re


def get_text_without_punctuation(text: str) -> str:
    return re.sub(r"[^A-Za-z\d\s]", "", text)
