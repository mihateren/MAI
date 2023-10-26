from itertools import permutations


def f(n):
    arr = []
    for i in range(n):
        arr.append(input())
    for x in permutations(sorted(arr), 3):
        print(', '.join(x))
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()