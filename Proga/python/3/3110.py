def f():
    s = input()
    counter = {"asd": -1}
    ans = ""
    while s != "ФИНИШ":
        for i in range(len(s)):
            keys = list(counter.keys())
            key = s[i]
            if s[i].lower() in keys:
                counter[s[i].lower()] += 1
            elif s[i].lower() != " ":
                counter[s[i].lower()] = 1 
        s = input()
    maxim = -1
    counterSorted = dict(sorted(counter.items()))
    for key, value in counterSorted.items():
        if counter[key] > maxim:
            maxim = value
            ans = key                
    print(ans)


def main():
    f()


if __name__ == '__main__':
    main()