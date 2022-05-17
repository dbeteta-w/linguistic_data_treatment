import re


def has_too_many_numbers(src: str, tgt: str, alpha=2):
    return not _has_too_many_numbers(src, alpha) \
           and not _has_too_many_numbers(tgt, alpha)


def _has_too_many_numbers(text: str, alpha=2):
    list_of_numbers = re.findall(r"\d", text)
    list_of_letters = re.findall(r"[A-Za-z]", text)
    if len(list_of_numbers) * alpha >= len(list_of_letters):
        return True
    return False
