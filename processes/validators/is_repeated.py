from typing import Set, Tuple

from processes.helpers.get_text_to_be_compared import get_text_to_be_compared


def is_repeated(src: str, tgt: str, set_tuple_src_tgt: Set[Tuple[str, str]]) -> bool:
    src_to_be_compared = get_text_to_be_compared(src)
    tgt_to_be_compared = get_text_to_be_compared(tgt)
    tuple_src_tgt = tuple([src_to_be_compared, tgt_to_be_compared])
    if tuple_src_tgt in set_tuple_src_tgt:
        return True
    return False


def is_text_repeated(text: str, set_texts: Set[str]):
    text_to_be_compared = get_text_to_be_compared(text)
    if text_to_be_compared in set_texts:
        return True
    return False
