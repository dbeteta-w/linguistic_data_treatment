import unicodedata


def get_text_with_normalized_accents(text: str) -> str:
    # NFC form (Normalization Form Canonical Composition) => accented letters = 1 character
    # For more info: https://en.wikipedia.org/wiki/Unicode_equivalence
    return unicodedata.normalize("NFC", text)
