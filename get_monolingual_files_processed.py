import os
import time
import fasttext
import argparse

from glob import glob
from functools import partial
from past.builtins import apply
from multiprocessing import Pool

from processes.helpers.get_text_to_be_compared import get_text_to_be_compared

from processes.normalizers.get_text_without_tags import get_text_without_tags
from processes.normalizers.get_text_without_initial_index import get_text_without_initial_index
from processes.normalizers.get_text_with_normalized_quotes import get_text_with_normalized_quotes
from processes.normalizers.get_text_with_normalized_spaces import get_text_with_normalized_spaces
from processes.normalizers.get_text_with_normalized_accents import get_text_with_normalized_accents
from processes.normalizers.get_text_without_repeated_symbols import get_text_without_repeated_symbols

from processes.validators.is_repeated import is_text_repeated
from processes.validators.has_too_many_numbers import has_text_too_many_numbers
from processes.validators.is_in_the_accurate_language import is_text_in_the_accurate_language
from processes.validators.has_a_properly_amount_of_words import has_text_properly_amount_of_words


def get_monolingual_files_processed(lang: str, path_to_file: str) -> None:
    with open(path_to_file, "r", encoding="utf-8") as fread, \
            open(args.output + "/output_monolingual_processed.txt", "a", encoding="utf-8") as fwrite:
        for text in fread:
            text_normalized = _normalize(text, lang)
            if _validate(text_normalized, lang):
                fwrite.write(text_normalized + "\n")


def _normalize(text: str, lang: str) -> str:
    list_of_normalizers = [
        get_text_without_initial_index,
        get_text_without_tags,
        get_text_with_normalized_accents,
        get_text_without_repeated_symbols,
        get_text_with_normalized_spaces
    ]

    for normalizer in list_of_normalizers:
        text = apply(normalizer, text)

    return get_text_with_normalized_quotes(text, lang)


def _validate(text: str, lang: str) -> bool:
    with open(args.output + "/" + lang + "_not_valid_texts.txt", "a", encoding="utf-8") as flog:
        if not has_text_properly_amount_of_words(text):
            flog.write(text + "|||has_text_properly_amount_of_words\n")
            return False
        if has_text_too_many_numbers(text):
            flog.write(text + "|||has_text_too_many_numbers\n")
            return False
        if not is_text_in_the_accurate_language(text, lang, fasttext_model):
            flog.write(text + "|||is_text_in_the_accurate_language\n")
            return False
        if is_text_repeated(text, set_texts):
            flog.write(text + "|||is_text_repeated\n")
            return False
        else:
            text_to_be_compared = get_text_to_be_compared(text)
            set_texts.add(text_to_be_compared)
    return True


if __name__ == "__main__":

    start = time.time()
    parser = argparse.ArgumentParser(
        description="Normalize and validate monolingual files"
    )
    parser.add_argument("-pi", "--input", type=str,
                        metavar="", required=True,
                        help="Path to the input files")
    parser.add_argument("-e", "--extension", type=str,
                        metavar="", required=True,
                        help="Extension of the files e.g. txt")
    parser.add_argument("-l", "--lang", type=str,
                        metavar="", required=True,
                        help="Language ISO 639-1 Code e.g en")
    parser.add_argument("-c", "--cpus", type=int,
                        metavar="", required=True,
                        help="Amount of cpus desired to use in the execution."
                             " Recommendation: use a max of 2/3 of the total")
    parser.add_argument("-po", "--output", type=str,
                        metavar="", required=True,
                        help="Path to the desired output place")

    args = parser.parse_args()

    set_texts = set()
    pretrained_model = "models/lid.176.bin"
    fasttext_model = fasttext.load_model(os.path.abspath(pretrained_model))

    if "." in args.extension:
        path_files_to_be_processed = glob(args.input + "/*" + args.extension)
    else:
        path_files_to_be_processed = glob(args.input + "/*." + args.extension)

    list_of_abs_path = []
    for file in path_files_to_be_processed:
        list_of_abs_path.append(os.path.abspath(file))
        print(file)

    main_function = partial(get_monolingual_files_processed, args.lang)

    with Pool(processes=args.cpus) as p:
        p.map(main_function, list_of_abs_path)

    print("Time needed:" + str((time.time() - start) / 60))
