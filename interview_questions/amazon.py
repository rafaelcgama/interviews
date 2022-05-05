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
from time import time
from itertools import combinations


def prod(arr):
    total = 1
    zero_idx, zero_count = 0, 0  # Can use a list for zero_idx/count but used a constant for better space complexity
    for i in range(len(arr)):
        if arr[i] != 0:
            total *= arr[i]
        else:
            zero_idx, zero_count = i, zero_count + 1
    return total, zero_idx, zero_count


def myproduct_with_zero(arr):
    result = [0] * len(arr)
    myprod, zero_idx, zero_count = prod(arr)
    if zero_count == 1:
        result[zero_idx] = myprod

    elif not zero_count:
        for i in range(len(arr)):
            result[i] = myprod / arr[i]

    return result


def myproduct_Onˆ2(arr):
    result = []
    for i in range(len(arr) - 1):
        cur_arr = arr[:i] + arr[i + 1:]
        result.append(math.prod(cur_arr))
    result.append(math.prod(arr[:-1]))

    return result
    # return list(map(lambda x: math.prod(x), combinations(mylist, len(mylist) - 1))) # If not needed to be in order


def myproduct_On(arr):
    result = []
    myprod = math.prod(arr)
    for i in range(len(arr)):
        result.append(myprod / arr[i])

    return result


mylist = list(range(1, 21))

result = []
start = time()
myproduct_Onˆ2(mylist)
result.append(time() - start)
print(result[0])
start = time()
myproduct_On(mylist)
result.append(time() - start)
print(result[1])
start = time()
myproduct_with_zero(mylist)
result.append(time() - start)
print(result[2])
start = time()
list(map(lambda x: math.prod(x), combinations(mylist, len(mylist) - 1)))
result.append(time() - start)
print(result[3])

print(result)
print(sorted(result))
