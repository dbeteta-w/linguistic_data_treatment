
def has_parallel_symbols_val(src: str, tgt: str, tolerance=0, symbols_to_check=None) -> bool:
    if symbols_to_check is None:
        symbols_to_check = {'[', ']', '{', '}', '<', '>', '@', '+', '...', '#'}

    for symbol in symbols_to_check:
        if abs(src.count(symbol) - tgt.count(symbol)) > tolerance:
            return False
    return True
