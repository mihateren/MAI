def make_linear(lists):
    result = []
    for x in lists:
        if isinstance(x, list):
            result.extend(make_linear(x))
        else:
            result.append(x)
    return result