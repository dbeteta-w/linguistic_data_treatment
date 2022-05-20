import re


def get_text_with_normalized_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
