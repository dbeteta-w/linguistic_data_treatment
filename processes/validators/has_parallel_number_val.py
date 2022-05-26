from text_to_num import alpha2digit


def has_parallel_number_val(src: str, src_lang: str, tgt: str, tgt_lang: str, tolerance=0) -> bool:
    src_alpha2digit = alpha2digit(src, src_lang)
    tgt_alpha2digit = alpha2digit(tgt, tgt_lang)
    for number in range(10):
        string_number = str(number)
        if abs(src.count(string_number) - tgt.count(string_number)) > tolerance and \
                abs(src_alpha2digit.count(string_number) - tgt_alpha2digit.count(string_number)) > tolerance:
            return False
    return True
