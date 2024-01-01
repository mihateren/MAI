def f(x, y):
    if x * x + y * y > 100:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    elif not inDanger(x, y):
        print("Зона безопасна. Продолжайте работу.")
    else:
        print("Опасность! Покиньте зону как можно скорее!")


def inDanger(x, y):
    #для параболы внизу y=0.25x^2+0.5x-8.75
    if (y < 0):
        if (0.25 * x * x + 0.5 * x - 8.75 <= y):
            return True
    elif (y == 0):
        if (x >= -7) and (x <= 5): 
            return True
    else:
        if (x >= -7) and (x <= -4): #прямая y=(5/3)*x+35/3
            if ((5 / 3) * x + (35 / 3) >= y):
                return True
        if (x > -4) and (x <= 0): #горизонтальная прямая y = 5
            if (y <= 5):
                return True
        if (x > 0) and (x < 5): #окружность в 1 четверти
            if (x * x + y * y <= 25):
                return True
    return False

    
def main():
    x = float(input())
    y = float(input())
    f(x, y)


if __name__ == '__main__':
    main()