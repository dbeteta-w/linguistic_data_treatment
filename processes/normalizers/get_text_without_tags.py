import re


def get_text_without_tags(text: str) -> str:
    # Remove html tags, tmx tags among other
    return re.sub(r"([<{]\\?/?[A-Za-z\d]+/?[>}]|[&%][A-Za-z\d]+;?)", "", text)
