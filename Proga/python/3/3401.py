def f(s):
    arr = list(s.split())
    n = [i for i in range(1, len(arr) + 1)]
    ans = list(zip(n, arr))
    for number, word in ans:
        print(f"{number}. {word}")
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()