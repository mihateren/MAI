def secret_replace(text, **kwargs):
    keys = []
    counters = []
    for key, value in kwargs.items():
        keys.append(key)
        counters.append(0)
    result = ''
    for char in text:
        if char in keys:
            key_index = keys.index(char)
            counter = counters[key_index]
            replacement_value = kwargs[char][counter % len(kwargs[char])]
            result += replacement_value
            counters[key_index] += 1
        else:
            result += char
    return result

