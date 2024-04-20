import pandas as pd
import string


def length_stats(text):
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    temp = text_no_punct.lower().split()
    temp = list(set(temp))
    temp.sort()
    odd_words = [word for word in temp if len(word) % 2 != 0]
    even_words = [word for word in temp if len(word) % 2 == 0]
    res_odd = pd.Series([len(word) for word in odd_words], index=odd_words, dtype='int64')
    res_even = pd.Series([len(word) for word in even_words], index=even_words, dtype='int64')
    return res_odd, res_even