def f(n, m, t):
    hours = n
    minuts = m
    minuts = (m + t) % 60
    hours = (n + int((m + t) / 60)) % 24
    hoursRes = "0" * (2 - len(str(hours))) + str(hours)
    minutsRes = "0" * (2 - len(str(minuts))) + str(minuts)
    print(f"{hoursRes}:{minutsRes}")
    

def main():
    n = int(input())
    m = int(input())
    t = int(input())
    f(n, m, t)


if __name__ == '__main__':
    main()