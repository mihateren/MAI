arr = []


def modern_print(s):
    global arr
    if s not in arr:
        arr.append(s)
        print(s)