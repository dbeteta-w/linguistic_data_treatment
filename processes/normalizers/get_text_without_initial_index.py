import re


def get_text_without_initial_index(text: str) -> str:
    not_number_found = re.findall(r"[^\d|,\t ]", text)
    if not_number_found:
        index_of_first_non_number = text.index(not_number_found[0])
        return re.sub(r"\d+[|,\t ]?", "", text[:index_of_first_non_number]) + text[index_of_first_non_number:]
    else:
        return text
