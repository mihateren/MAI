def f(s1, s2):
    arr1 = list(s1.split(", "))
    arr2 = list(s2.split(", "))
    ans = zip(arr1, arr2)
    for p1, p2 in ans:
        print(f"{p1} - {p2}")
    

def main():
    s1 = input()
    s2 = input()
    f(s1, s2)


if __name__ == '__main__':
    main()