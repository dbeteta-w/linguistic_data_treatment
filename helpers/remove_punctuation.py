import string


def remove_punctuation(text: str) -> str:
    extra_punctuation = ["¿", "¡"]
    punctuation = list(string.punctuation)
    punctuation.extend(extra_punctuation)

    for punct in punctuation:
        text = text.replace(punct, "")
    return text
