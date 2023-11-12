def can_eat(horse, figure):
    hx, hy = horse
    fx, fy = figure
    if (abs(hx - fx) == 2 and abs(hy - fy) == 1) or (abs(hx - fx) == 1 and abs(hy - fy) == 2):
        return True
    return False