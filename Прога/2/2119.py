def f(name, price, weight, money):
    print("================Чек================")
    print("Товар:" + name.rjust(29))
    print("Цена:" + f"{weight}кг * {price}руб/кг".rjust(30))
    print("Итого:{0:26d}руб".format(price * weight))
    print("Внесено:{0:24d}руб".format(money))
    print("Сдача:{0:26d}руб".format(money - price * weight))
    print("===================================")
    

def main():
    name = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    f(name, price, weight, money)


if __name__ == '__main__':
    main()