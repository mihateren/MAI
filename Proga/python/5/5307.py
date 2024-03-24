class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    alph = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    if not isinstance(name, str):
        raise TypeError
    for c in name:
        if c.lower() not in alph:
            raise CyrillicError
    if name != name.lower().capitalize():
        raise CapitalError
    return name