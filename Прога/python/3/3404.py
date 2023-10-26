from itertools import count

def f(s):
    arr = s.split()
    ans = ""
    for i in count(0, 1):
        if i > len(arr) - 1:
            break
        ans += arr[i] + " "
        print(ans[:-1])


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()