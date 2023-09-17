def checque(product_name, price, weight, money):
    print("Чек")
    print(f"{product_name} - {weight}кг - {price}руб/кг")
    total = weight * price
    print(f"Итого: {total}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - total}руб")


def main():
    product_name = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    checque(product_name, price, weight, money)


if __name__ == '__main__':
    main()