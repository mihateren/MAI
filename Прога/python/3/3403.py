from itertools import count

def f(s):
    start, end, step = map(float, s.split())
    for x in count(start, step):
        if x > end: 
            break
        print(f"{x:.2f}")
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()