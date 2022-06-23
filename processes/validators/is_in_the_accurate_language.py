from processes.normalizers.get_text_with_normalized_spaces import get_text_with_normalized_spaces


def is_in_the_accurate_language(src: str, src_lang: str, tgt: str, tgt_lang: str,
                                fasttext_model, minimum_probability=0.4) -> bool:
    return is_text_in_the_accurate_language(src, src_lang, fasttext_model, minimum_probability) \
           and is_text_in_the_accurate_language(tgt, tgt_lang, fasttext_model, minimum_probability)


def is_text_in_the_accurate_language(text: str, lang: str, fasttext_model, minimum_probability=0.4) -> bool:
    AMOUNT_OF_GUESSES = 2
    LABEL_TYPO = "__label__"
    text_with_normalized_spaces = get_text_with_normalized_spaces(text)

    guess_array = fasttext_model.predict(text_with_normalized_spaces, k=AMOUNT_OF_GUESSES)
    if len(guess_array) >= AMOUNT_OF_GUESSES \
            and len(guess_array[0]) >= AMOUNT_OF_GUESSES \
            and len(guess_array[1]) >= AMOUNT_OF_GUESSES:
        first_lang_guess = guess_array[0][0].replace(LABEL_TYPO, "")
        first_lang_prob = guess_array[1][0]
        if first_lang_guess != lang or \
                (first_lang_guess == lang and
                 first_lang_prob < minimum_probability):
            second_lang_guess = guess_array[0][1].replace(LABEL_TYPO, "")
            second_lang_prob = guess_array[1][1]
            if second_lang_guess != lang or \
                    (second_lang_guess == lang and
                     second_lang_prob < minimum_probability):
                return False
    return True
