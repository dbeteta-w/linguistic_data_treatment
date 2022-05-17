import string


def remove_punctuation(text: str) -> str:
    for punct in string.punctuation:
        text = text.replace(punct, "")
    return text
