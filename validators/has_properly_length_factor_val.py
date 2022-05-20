from helpers.get_text_to_be_compared import get_text_to_be_compared


def has_properly_length_factor_val(src: str, tgt: str, length_factor=2.0, min_len=6) -> bool:
    len_src_to_be_compared = len(get_text_to_be_compared(src))
    len_tgt_to_be_compared = len(get_text_to_be_compared(tgt))

    if len_src_to_be_compared < min_len and len_tgt_to_be_compared < min_len:
        return True
    if len_src_to_be_compared > len_tgt_to_be_compared * length_factor \
            or len_tgt_to_be_compared > len_src_to_be_compared * length_factor:
        return False
    return True
