from enum import Enum


class MetaQuote(Enum):
    OPEN = 1
    CLOSE = 2
    FOUND = 3


# Source: #https://en.wikipedia.org/wiki/Quotation_mark
MAIN_QUOTES_PER_LANG = {
    "universal_simple": {
        MetaQuote.OPEN: "'",
        MetaQuote.CLOSE: "'"
    },
    "universal_double": {
        MetaQuote.OPEN: '"',
        MetaQuote.CLOSE: '"'
    },
    'cz': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'da': {
        MetaQuote.OPEN: '»',
        MetaQuote.CLOSE: '«'
    },
    'de': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'en': {
        MetaQuote.OPEN: '‘',
        MetaQuote.CLOSE: '’'
    },
    'es': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'fr': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'hr': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '”'
    },
    'it': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'nl': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'mt': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'pt': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'pl': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '”'
    },
    'sq': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'ar': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'hy': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'az': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'eu': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'be': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'bo': {
        MetaQuote.OPEN: '《',
        MetaQuote.CLOSE: '》'
    },
    'bs': {
        MetaQuote.OPEN: '”',
        MetaQuote.CLOSE: '”'
    },
    'bg': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'ca': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'cs': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'zh': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'el': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'et': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'fa': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'ro': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '”'
    },
    'ru': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'sk': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'sl': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '“'
    },
    'sr': {
        MetaQuote.OPEN: '„',
        MetaQuote.CLOSE: '”'
    },
    'sv': {
        MetaQuote.OPEN: '”',
        MetaQuote.CLOSE: '”'
    },
    'ta': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'th': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'ti': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'tr': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'uk': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'ur': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'ug': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'uz': {
        MetaQuote.OPEN: '«',
        MetaQuote.CLOSE: '»'
    },
    'vi': {
        MetaQuote.OPEN: '“',
        MetaQuote.CLOSE: '”'
    },
    'cy': {
        MetaQuote.OPEN: '‘',
        MetaQuote.CLOSE: '’'
    },
    'ko': {
        MetaQuote.OPEN: '‘',
        MetaQuote.CLOSE: '’'
    },
    'ja': {
        MetaQuote.OPEN: '「',
        MetaQuote.CLOSE: '」'
    }
}


def get_text_with_normalized_quotes(text: str, lang_desired: str) -> str:
    rest_quotes = {
        quote for lang, quotes in MAIN_QUOTES_PER_LANG.items() for _, quote in quotes.items() if lang != lang_desired
    }

    amount_quotes = 0
    for quote in rest_quotes:
        amount_quotes += text.count(quote)
        text = text.replace(quote, str(MetaQuote.FOUND))

    amount_replacements = 1
    if amount_quotes == 0:
        return text
    elif amount_quotes % 2 == 0:
        for iteration in range(amount_quotes):
            if iteration % 2 == 0:
                text = text.replace(
                    str(MetaQuote.FOUND), MAIN_QUOTES_PER_LANG[lang_desired][MetaQuote.OPEN], amount_replacements
                )
            else:
                text = text.replace(
                    str(MetaQuote.FOUND), MAIN_QUOTES_PER_LANG[lang_desired][MetaQuote.CLOSE], amount_replacements
                )
    else:
        text = text.replace(str(MetaQuote.FOUND), "")
    return text
