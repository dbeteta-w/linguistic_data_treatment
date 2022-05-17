from typing import Set, Tuple

from helpers.clean_to_be_compared import clean_to_be_compared


def is_repeated(src: str, tgt: str, set_tuple_src_tgt: Set[Tuple[str, str]]):
    src_to_be_compared = clean_to_be_compared(src)
    tgt_to_be_compared = clean_to_be_compared(tgt)
    tuple_src_tgt = tuple([src_to_be_compared, tgt_to_be_compared])
    if tuple_src_tgt in set_tuple_src_tgt:
        return True
    return False
