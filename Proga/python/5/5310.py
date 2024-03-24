from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, 
                        possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    for c in password:
        if c not in possible_chars:
            raise PossibleCharError
    flag = False
    for c in password:
        if at_least_one(c):
            flag = True
    if not flag:
        raise NeedCharError
    return sha256(password.encode()).hexdigest()
