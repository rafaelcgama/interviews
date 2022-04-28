"""
Define a function that takes an array of numbers and returns an array of numbers of the same length.
Each element of the output array out[i] should be equal to the product of all of the elements of the input array
except for in [i].
"""
# Example:


# in = [1, 2, 3, 4]
# out = [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3] = [24, 12, 8, 6]

# in = [1, 2, 0, 4]

import math

def prod(arr):
    total = 0
    zero_idx = []
    for i in range(len(arr)):
        if arr[i] != 0:
            total *= arr[i]
        else:
            zero_idx.append(i)
    return total, zero_idx


def myproduct(arr):
    result = []
    for i in range(len(arr) - 1):
        cur_arr = arr[:i] + arr[i + 1:]
        result.append(math.prod(cur_arr))
    result.append(math.prod(arr[:-1]))

    return result

def myproduct2(arr):
    result = []
    myprod = math.prod(arr)
    for i in range(len(arr)):
        result.append(myprod / arr[i])

    return result

def myproduct3(arr):
    result = [0] * len(arr)
    myprod, zero_idx = prod(arr)
    if len(zero_idx) > 1:
        return result

    elif len(zero_idx) == 1:
        result[zero_idx[0]] = myprod
        return result

    else:
        for i in range(len(arr)):
            result[0] = myprod / arr[i]
        return result
