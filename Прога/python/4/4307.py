def same_type(func):
    def wrapper(*args):
        types = []
        for x in args:
            types.append(type(x))
        if len(set(types)) > 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return wrapper