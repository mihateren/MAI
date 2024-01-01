def f(n):
    max_number = n
    all_lengths = []
    counter = 1
    cocounter = 1
    intermidate_var = []
    for i in range(1, max_number + 1):
        intermidate_var.append(str(i))
        if len(intermidate_var) == counter:
            all_lengths.append(' '.join(intermidate_var))
            intermidate_var = []
            counter += 1
    if intermidate_var != []:
        all_lengths.append(' '.join(intermidate_var))
    for i in all_lengths:
        print(f'{" " * ((len(all_lengths[-1]) - len(i)) // 2)}{i}')

                
def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()