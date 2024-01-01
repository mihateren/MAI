def recursive_sum(*args):
    sum = 0
    if len(args) == 1:
        return args[0]
    newArgs = args[1:]
    sum = args[0] + recursive_sum(*newArgs)
    return sum