def make_equation(*args):
    ans = str(args[-1])
    if len(args) == 1:
        return str(args[0])
    newArgs = args[:-1]
    ans = f"({make_equation(*newArgs)}) * x + {ans}"
    return ans