class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    aNum = isinstance(a, float) or isinstance(a, int)
    bNum = isinstance(b, float) or isinstance(b, int)
    cNum = isinstance(c, float) or isinstance(c, int)
    if not (aNum and bNum and cNum):
        raise TypeError()
    elif not (a or b or c):
        raise InfiniteSolutionsError()
    elif not a and not b and c or b**2 < 4 * a * c:
        raise NoSolutionsError()
    elif b ** 2 == 4 * a * c:
        return -b / (2 * a), -b / (2 * a)
    elif not a:
        return -c / b
    else:
        roots = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
        roots.sort()
        return roots[0], roots[1]
    
