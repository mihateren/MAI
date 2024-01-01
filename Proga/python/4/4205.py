def to_string(*keys, sep=" ", end="\n"):
    result = ""
    for x in keys:
        result += str(x)
        if keys.index(x) + 1 != len(keys):
            result += sep
    return result + end
    