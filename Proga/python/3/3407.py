from itertools import combinations


def f(n):
    players = []
    for i in range(n):
        players.append(input())
    for x, y in list(combinations(players, 2)):
        print(f"{x} - {y}")
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()