from text_to_num import alpha2digit


def has_parallel_number_val(src: str, tgt: str, src_lang: str, tgt_lang: str) -> bool:
    src_alpha2digit = alpha2digit(src, src_lang)
    tgt_alpha2digit = alpha2digit(tgt, tgt_lang)
    for number in range(10):
        number_to_be_counted = str(number)
        if src.count(number_to_be_counted) != tgt.count(number_to_be_counted) and \
                src_alpha2digit.count(number_to_be_counted) != tgt_alpha2digit.count(number_to_be_counted):
            return False
    return True
