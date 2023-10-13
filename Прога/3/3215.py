def f():
    s = input()
    numbers10 = list(map(int, s.split()))
    numbers2 = []
    for num in numbers10:
        numbers2.append(format(num, 'b'))
    ans = []
    for i in range(len(numbers2)):
        ans.append({'digits': 0, 'units': 0, 'zeros': 0})
    for i in range(len(numbers2)):
        num = numbers2[i]
        units = 0
        zeros = 0
        ans[i]['digits'] = len(num)
        for j in range(len(num)):
            if num[j] == '1':
                units += 1
            else:
                zeros += 1
        ans[i]['units'] = units
        ans[i]['zeros'] = zeros
    print(ans)


def main():
    f()


if __name__ == '__main__':
    main()