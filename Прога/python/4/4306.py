def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a, b = arr[:mid], arr[mid:]
        ans = merge(merge_sort(a), merge_sort(b))
    return ans


def merge(a, b):
    arr = []
    cA, cB = 0, 0
    while (cA != len(a) and cB != len(b)):
        if (a[cA] >= b[cB]):
            arr.append(b[cB])
            cB += 1
        else:
            arr.append(a[cA])
            cA += 1
    arr += a[cA:]
    arr += b[cB:]
    return arr