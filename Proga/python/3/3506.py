def f():
    letters = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
               'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
               'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
               'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'Ь': '', 'Ъ': ''}
    inp, out = "", ""
    with open("cyrillic.txt") as file_in:
        for line in file_in:
            inp += line
    for x in inp:
        if x.upper() in letters:
            if x == x.upper():
                out += letters[x.upper()]
            else:
                out += letters[x.upper()].lower()
        else:
            out += x
    with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
        file_out.write(out)
           

def main():
    f()


if __name__ == '__main__':
    main()