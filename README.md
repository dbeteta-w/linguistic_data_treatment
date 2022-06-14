# Linguistic Data Treatment

![Contributors](https://img.shields.io/github/contributors/dbeteta-w/linguistic_data_treatment)
![Forks](https://img.shields.io/github/forks/dbeteta-w/linguistic_data_treatment)
![Stars](https://img.shields.io/github/stars/dbeteta-w/linguistic_data_treatment)
![Licence](https://img.shields.io/github/license/dbeteta-w/linguistic_data_treatment) 
![Issues](https://img.shields.io/github/issues/dbeteta-w/linguistic_data_treatment) 

### Description

The purpose of this repo is to bring together the main cleaning processes 
in order to get the most value from a dirty linguistic dataset.

In such way, it's divided the concept of "cleaning process" into two:

1. Normalizers: which goal is to give consistency to the entire dataset =>
[EXAMPLE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_without_repeated_symbols.py)
2. Validators: which goal is to check if a piece of the dataset is valuable or not  =>
[EXAMPLE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/is_repeated.py)

In the same line, there are another type of functions which are called "Helpers"
and its goal is to avoid rewriting functions that are used mainly in the normalizers and the validators 
=> [EXAMPLE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/helpers/get_text_to_be_compared.py)

Last but not least, it's important that you know that these processes are made to be able to process both monolingual
and bilingual datasets => [EXAMPLE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_too_many_numbers.py)

### Recommended Usage

You can find a clear example of usage for monolingual datasets [HERE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/get_monolingual_files_processed.py)
and for bilingual datasets [HERE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/get_bilingual_files_processed.py).

What it's done is, on the one hand bringing all the desired normalizers into just one function with the purpose of 
defining what it's understood for "normalize" in this particular case. And, in the other hand, it's done a similar thing for "validate"
with the particularity that in this case it's made to keep track of the invalid parts of the dataset. 

#### Note: You want to use certain "cleaning processes" or other depending on the language(s) of the dataset to be treated. 

### Perspective of future

Although the origin of this repo is made thinking mainly of the English-Spanish combination, it's expected 
to increase the amount of "cleaning processes" in order to reach the most languages as possible.

### Contribution Guidelines

The contribution guidelines are as per the guide [HERE](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/CONTRIBUTING.md).

### Instructions

- Fork this Repository
- Clone your forked repository
- Add your process
- Commit & Push
- Create a pull request
- Star this repository
- Wait for Pull Request to merge
- Celebrate, your first step into the open Source World and contribute more

#### Note: When you Add a process Add it to the README for ease of solving any kind of issue

### Current Cleaning Processes
| Nº  | Cleaning Process                                                                                                                                                                     | Author                                        |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 1   | [Has A Properly Amount Of Words](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_a_properly_amount_of_words.py)                            | [Daniel Beteta](https://github.com/dbeteta-w) |
| 2   | [Has Parallel Number Val](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_parallel_number_val.py)                                          | [Daniel Beteta](https://github.com/dbeteta-w) |
| 3   | [Has Parallel Symbol Val](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_parallel_symbols_val.py)                                         | [Daniel Beteta](https://github.com/dbeteta-w) |
| 4   | [Has Properly Length Factor Val](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_properly_length_factor_val.py)                            | [Daniel Beteta](https://github.com/dbeteta-w) |
| 5   | [Has Too Many Numbers](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/has_too_many_numbers.py)                                                | [Daniel Beteta](https://github.com/dbeteta-w) |
| 6   | [Is In The Accurate Language](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/is_in_the_accurate_language.py)                                  | [Daniel Beteta](https://github.com/dbeteta-w) |
| 7   | [Is Repeated](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/validators/is_repeated.py)                                                                  | [Daniel Beteta](https://github.com/dbeteta-w) |
| 8   | [Get Text With Normalized Quotes](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_with_normalized_quotes.py)                         | [Daniel Beteta](https://github.com/dbeteta-w) |
| 9   | [Get Text With Normalized Spaces](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_with_normalized_spaces.py)                         | [Daniel Beteta](https://github.com/dbeteta-w) |
| 10  | [Get Text With Normalized Unicode Characters](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_with_normalized_unicode_characters.py) | [Daniel Beteta](https://github.com/dbeteta-w) |
| 11  | [Get Text Without Initial Index](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_without_initial_index.py)                           | [Daniel Beteta](https://github.com/dbeteta-w) |
| 12  | [Get Text Without Repeated Symbols](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_without_repeated_symbols.py)                     | [Daniel Beteta](https://github.com/dbeteta-w) |
| 13  | [Get Text Without Tags](https://github.com/dbeteta-w/linguistic_data_treatment/blob/main/processes/normalizers/get_text_without_tags.py)                                             | [Daniel Beteta](https://github.com/dbeteta-w) |
