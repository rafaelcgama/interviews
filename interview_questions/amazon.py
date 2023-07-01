## 238. Product of Array Except Self (Leet Code)

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

# # Does not work in leetcode
# def myproduct_with_zero(arr):
#     result = [0] * len(arr)
#     zero_count = arr.count(0)
#     if not zero_count:
#         for i in range(len(arr)):
#             result[i] = math.prod(arr) // arr[i]
#
#     elif zero_count == 1:
#         new_arr, zero_idx = list(arr), arr.index(0)
#         del new_arr[zero_idx]
#         result[zero_idx] = math.prod(new_arr)
#
#     return result

def myproduct_with_zero(nums):
    def prod(arr):
        total = 1
        zero_idx = []
        for i in range(len(arr)):
            if arr[i] != 0:
                total *= arr[i]
            else:
                zero_idx.append(i)
                if len(zero_idx) == 2:
                    break
        return total, zero_idx

    result = [0] * len(nums)
    myprod, zero_idx = prod(nums)
    if not zero_idx:
        for i in range(len(nums)):
            result[i] = myprod // nums[i]

    elif len(zero_idx) == 1:
        result[zero_idx[0]] = myprod

    return result


def myproduct_Onˆ2(arr):
    result = []
    for i in range(len(arr) - 1):
        cur_arr = arr[:i] + arr[i + 1:]
        result.append(math.prod(cur_arr))
    result.append(math.prod(arr[:-1]))

    return result
    # return list(map(lambda x: math.prod(x), combinations(reversed(mylist), len(mylist) - 1))) # Inefficient


def myproduct_On(arr):
    # Solution without input that includes zeros
    result = []
    myprod = math.prod(arr)
    for i in range(len(arr)):
        result.append(myprod / arr[i])

    return result


seqs = [[1, 2, 3, 4], [-1, 1, 0, -3, 3], [0, 0, 2, 4, 5]]
for s in seqs:
    print(myproduct_with_zero(s))

# mylist = list(range(1, 21))
#
# result = []
# start = time()
# myproduct_Onˆ2(mylist)
# result.append(time() - start)
# print(result[0])
# start = time()
# myproduct_On(mylist)
# result.append(time() - start)
# print(result[1])
# start = time()
# myproduct_with_zero(mylist)
# result.append(time() - start)
# print(result[2])
# start = time()
# list(map(lambda x: math.prod(x), combinations(mylist, len(mylist) - 1)))
# result.append(time() - start)
# print(result[3])
#
# print(result)
# print(sorted(result))
