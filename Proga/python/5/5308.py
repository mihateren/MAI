class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    alph = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    digits = '0123456789'
    if not isinstance(username, str):
        raise TypeError
    for c in username:
        if c.lower() not in alph:
            raise BadCharacterError
    if username[0] in digits:
        raise StartsWithDigitError
    return username
    