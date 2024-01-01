def recursive_digit_sum(n):
    sum = 0
    if n < 10:
        return n
    newArgs = n // 10
    sum += n % 10 + recursive_digit_sum(newArgs)
    return sum
