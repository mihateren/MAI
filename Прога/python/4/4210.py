def secret_replace(s, **kwargs):
    ans = ""
    n = [0] * len(kwargs.keys())
    for x in s:
        if x in list(kwargs.keys()):
            xIndex = list(kwargs.keys()).index(x)
            ans += kwargs[x][n[xIndex] % len(kwargs[x])]
            n[xIndex] += 1
        else:
            ans += x
    return ans