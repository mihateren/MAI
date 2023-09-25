def f(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{j} * {i} = {j * i}")
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()