import spacy
from collections import Counter

def count_words_returns_dic(word_list):
    nlp = spacy.load("pt_core_news_sm")
    nlp.Defaults.stop_words |= {'ccee', 'n', 'linkx', 'ltda', '\n\n', '\n', '\n\n\n\n \n\n', '\n \n\n'}
    file = nlp(word_list)
    nouns = [
        token.text.lower() for token in file if
        token.is_stop is False
        and token.is_punct is False
        and token.pos_ != "NUM"
        and token.pos_ != "PRON"
        and token.pos_ != "SYM"
        and len(token) > 3
    ]

    noun_freq = Counter(nouns)
    common_nouns = noun_freq.most_common(30)
    dct = dict((y, x) for y, x in common_nouns)
    return dct