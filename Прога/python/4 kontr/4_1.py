def index(text):
    letters = list(text)
    letters.sort()
    set_letters = set()
    for x in letters:
        if x not in set_letters and x.isalpha():
            count_letter = text.index(x)
            pair = [x, count_letter]
            set_letters.add(x)
            yield tuple(pair)