import pandas as pd


def get_long(data, min_length=5):
    return data[data >= min_length]