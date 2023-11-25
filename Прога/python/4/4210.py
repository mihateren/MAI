# def secret_replace(s, **kwargs):
#     ans = ""
#     n = [0] * len(kwargs.keys())
#     for x in s:
#         if x in list(kwargs.keys()):
#             xIndex = list(kwargs.keys()).index(x)
#             ans += kwargs[x][n[xIndex] % len(kwargs[x])]
#             n[xIndex] += 1
#         else:
#             ans += x
#     return ans


def secret_replace(s, **replacements):
    for key, values in replacements.items():
        for value in values:
            s = s.replace(value, key)
    return s

result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)


