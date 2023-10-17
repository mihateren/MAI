def f():
    alph = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
    }
    ban = "ЬьЪъ"
    s = input()
    ans = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] not in ban:
                letter = alph[s[i].upper()]
                if s[i].lower() != s[i]:
                    if len(letter) > 1:
                        ans += letter[0] + letter[1:].lower()
                    else:
                        ans += letter
                else:
                    ans += letter.lower()
        else:
            ans += s[i]
    print(ans)


def main():
    f()


if __name__ == "__main__":
    main()
