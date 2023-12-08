def counter(text):
    text = text.replace(' ', '')
    letters = list(text)
    letters.sort()
    set_letters = set()
    for x in letters:
        if x not in set_letters:
            count_letter = letters.count(x)
            pair = [x, count_letter]
            set_letters.add(x)
            yield tuple(pair)


text = 'Мама мыла раму' 
for letter, i in counter(text):
    print(f'{letter}: {i}')