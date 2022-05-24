import re

from typing import List


def get_text_without_repeated_symbols(text: str) -> str:
    symbols_found = _get_symbols(text)
    indexes_symbols_found = _get_indexes_of_symbols(text, symbols_found)
    subset_of_indexes_followed = _get_subset_of_indexes_followed(indexes_symbols_found)
    return _remove_repeated_symbols(text, subset_of_indexes_followed)


def _get_symbols(text: str) -> List[str]:
    return re.findall(r"[^A-Za-z\d\s]", text)


def _get_indexes_of_symbols(text: str, symbols_found: List[str]) -> List[int]:
    indexes_symbols_found = []
    for symbol in symbols_found:
        if not indexes_symbols_found:
            indexes_symbols_found.append(text.index(symbol))
        else:
            new_start = indexes_symbols_found[-1] + 1
            indexes_symbols_found.append(text.index(symbol, new_start))
    return indexes_symbols_found


def _get_subset_of_indexes_followed(indexes_symbols_found: List[int]) -> List[List[int]]:
    subset_of_indexes_followed = []
    for index, next_index in zip(indexes_symbols_found, indexes_symbols_found[1:]):
        if next_index - index == 1:
            subset_of_indexes_followed.append([index, next_index])
    return subset_of_indexes_followed


def _remove_repeated_symbols(text: str, subset_of_indexes_followed: List[List[int]]) -> str:
    for i, subset in enumerate(subset_of_indexes_followed):
        index, next_index = subset
        text = text[:next_index - i] + text[(next_index + 1) - i:]
    return text
