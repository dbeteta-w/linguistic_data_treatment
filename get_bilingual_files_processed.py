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

from processes.validators.is_repeated import is_repeated
from processes.validators.has_too_many_numbers import has_too_many_numbers
from processes.validators.has_parallel_number_val import has_parallel_number_val
from processes.validators.has_parallel_symbols_val import has_parallel_symbols_val
from processes.validators.is_in_the_accurate_language import is_in_the_accurate_language
from processes.validators.has_properly_length_factor_val import has_properly_length_factor_val
from processes.validators.has_a_properly_amount_of_words import has_a_properly_amount_of_words


def get_bilingual_files_processed(src_lang: str, tgt_lang: str, path_to_file: str) -> None:
    with open(path_to_file, "r", encoding="utf-8") as fread, \
            open(args.output + "/output_bilingual_processed.txt", "a", encoding="utf-8") as fwrite:
        for text in fread:
            src, tgt = text.split(SEPARATOR)
            src_normalized, tgt_normalized = _normalize(src, src_lang), _normalize(tgt, tgt_lang)
            if _validate(src_normalized, src_lang, tgt_normalized, tgt_lang):
                fwrite.write(src_normalized + SEPARATOR + tgt_normalized + "\n")


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


def _validate(src: str, src_lang: str, tgt: str, tgt_lang: str) -> bool:
    with open(args.output + "/" + src_lang + "_" + tgt_lang + "_not_valid_texts.txt", "a", encoding="utf-8") as flog:
        if not has_a_properly_amount_of_words(src, tgt, MIN_WORDS, MAX_WORDS):
            flog.write(src + "|||" + tgt + "|||has_a_properly_amount_of_words\n")
            return False
        if has_too_many_numbers(src, tgt, ALPHA_VALUE):
            flog.write(src + "|||" + tgt + "|||has_too_many_numbers\n")
            return False
        if not is_in_the_accurate_language(src, src_lang, tgt, tgt_lang, FASTTEXT_MODEL, MIN_PROBABILITY):
            flog.write(src + "|||" + tgt + "|||is_in_the_accurate_language\n")
            return False
        if not has_properly_length_factor_val(src, tgt, LENGTH_FACTOR):
            flog.write(src + "|||" + tgt + "|||has_properly_length_factor_val\n")
            return False
        if not has_parallel_symbols_val(src, tgt, TOLERANCE_SYMBOLS):
            flog.write(src + "|||" + tgt + "|||has_parallel_symbols_val\n")
            return False
        if not has_parallel_number_val(src, src_lang, tgt, tgt_lang, TOLERANCE_NUMBERS):
            flog.write(src + "|||" + tgt + "|||has_parallel_number_val\n")
            return False
        if is_repeated(src, tgt, set_texts):
            flog.write(src + "|||" + tgt + "|||is_repeated\n")
            return False
        else:
            src_to_be_compared, tgt_to_be_compared = get_text_to_be_compared(src), get_text_to_be_compared(tgt)
            set_texts.add(tuple([src_to_be_compared, tgt_to_be_compared]))
    return True


if __name__ == "__main__":

    start = time.time()
    parser = argparse.ArgumentParser(
        description="Normalize and validate bilingual files"
    )
    parser.add_argument(
        "-pi", "--input", type=str, required=True,
        help="Path to the input files"
    )
    parser.add_argument(
        "-e", "--extension", type=str, required=True,
        choices=[".tsv", ".csv"],
        help="Extension of the files"
    )
    parser.add_argument(
        "-sc", "--srccode", type=str, required=True,
        help="Source language ISO 639-1 Code => en"
    )
    parser.add_argument(
        "-tc", "--tgtcode", type=str, required=True,
        help="Target language ISO 639-1 Code => es"
    )
    parser.add_argument(
        "-c", "--cpus", type=int, required=True,
        help="Amount of cpus desired to use in the execution.\n"
             "Recommendation: use a max of 2/3 of the total"
    )
    parser.add_argument(
        "-po", "--output", type=str, required=True,
        help="Path to the desired output folder"
    )
    parser.add_argument(
        "-opt", "--optional", required=False, nargs=7,
        metavar=("MIN_WORDS", "MAX_WORDS", "ALPHA", "MIN_PROB",
                 "LENGTH_FACTOR", "TOLERANCE_SYMBOLS", "TOLERANCE_NUMBERS"),
        help="Introduce the seven values like => 2 35 2 0.4 2.0 0 0\n"
             "1. Minimum words => has_a_properly_amount_of_words - \n"
             "2. Maximum words => has_a_properly_amount_of_words - \n"
             "3. Alpha value => ------ has_too_many_numbers ------ \n"
             "4. Min probability => - is_in_the_accurate_language -\n"
             "5. Length factor => - has_properly_length_factor_val \n"
             "6. Tolerance wrong symbol => has_parallel_symbols_val\n"
             "7. Tolerance wrong number => has_parallel_number_val \n"
             "If you want the default value just introduce -1 "
             "in the desired variable => 2 35 -1 0.5 2.0 -1 0"
    )

    args = parser.parse_args()

    set_texts = set()
    pretrained_model = "models/lid.176.bin"
    FASTTEXT_MODEL = fasttext.load_model(os.path.abspath(pretrained_model))

    # By default values
    MIN_WORDS, MAX_WORDS, ALPHA_VALUE, MIN_PROBABILITY, LENGTH_FACTOR, TOLERANCE_SYMBOLS, TOLERANCE_NUMBERS \
        = 2, 35, 2, 0.4, 2, 0, 0,

    if args.optional:
        MIN_WORDS = int(args.optional[0]) if int(args.optional[0]) != -1 else MIN_WORDS
        MAX_WORDS = int(args.optional[1]) if int(args.optional[1]) != -1 else MAX_WORDS
        ALPHA_VALUE = int(args.optional[2]) if int(args.optional[2]) != -1 else ALPHA_VALUE
        MIN_PROBABILITY = float(args.optional[3]) if float(args.optional[3]) != -1 else MIN_PROBABILITY
        LENGTH_FACTOR = float(args.optional[4]) if float(args.optional[4]) != -1 else LENGTH_FACTOR
        TOLERANCE_SYMBOLS = float(args.optional[5]) if float(args.optional[5]) != -1 else TOLERANCE_SYMBOLS
        TOLERANCE_NUMBERS = float(args.optional[6]) if float(args.optional[6]) != -1 else TOLERANCE_NUMBERS

    path_files_to_be_processed = glob(args.input + "/*" + args.extension)
    SEPARATOR = "\t" if args.extension == ".tsv" else ","

    list_of_abs_path = []
    for file in path_files_to_be_processed:
        list_of_abs_path.append(os.path.abspath(file))
        print(file)

    main_function = partial(get_bilingual_files_processed, args.srccode.lower(), args.tgtcode.lower())

    with Pool(processes=args.cpus) as p:
        p.map(main_function, list_of_abs_path)

    print("Time needed:" + str((time.time() - start) / 60))
