def is_palindrome(a):
    if isinstance(a, int) or isinstance(a, str):
        if str(a) == str(a)[::-1]:
            return True
    if isinstance(a, list) or isinstance(a, tuple):
        if list(a) == list(reversed(a)):
            return True
    return False
