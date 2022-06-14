import unicodedata


def get_text_with_normalized_unicode_characters(text: str) -> str:
    # NFD form (Normalization Form Canonical Decomposition) => accented letters = 2 character
    # For more info: https://en.wikipedia.org/wiki/Unicode_equivalence
    return unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("UTF-8")
