class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
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


def username_validation(username):
    alph = "abcdefghijklmnopqrstuvwxyz0123456789_"
    digits = "0123456789"
    if not isinstance(username, str):
        raise TypeError
    for c in username:
        if c.lower() not in alph:
            raise BadCharacterError
    if username[0] in digits:
        raise StartsWithDigitError
    return username


def user_validation(**kwargs):
    true_args = ["last_name", "first_name", "username"]
    for arg in kwargs:
        if arg not in true_args:
            raise KeyError
    if len(kwargs) != 3:
        raise KeyError
    for arg in kwargs:
        if not isinstance(arg, str):
            raise TypeError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
