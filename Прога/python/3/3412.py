def f(n):
    arr = []
    for i in range(n):
        arr += input().split(", ")
    iter = [int(i) for i in range(1, len(arr) + 1)]
    ans = zip(iter, sorted(arr))
    for number, word in ans:
        print(f"{number}. {word}")
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()