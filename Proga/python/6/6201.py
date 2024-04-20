import pandas as pd
import string


def length_stats(text):
    temp = text.translate(str.maketrans('', '', string.punctuation))
    temp = temp.lower().split()
    temp = list(set(temp))
    temp.sort()
    res = pd.Series([len(i) for i in temp], index=temp)
    return res