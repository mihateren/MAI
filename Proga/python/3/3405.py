def f(s1, s2, s3):
    arr = s1.split(", ") + s2.split(", ") + s3.split(", ")
    iter = [int(i) for i in range(1, len(arr) + 1)]
    ans = zip(iter, sorted(arr))
    for number, word in ans:
        print(f"{number}. {word}")
    

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    f(s1, s2, s3)


if __name__ == '__main__':
    main()