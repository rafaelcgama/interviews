## 238. Product of Array Except Self (Leet Code)

"""
Define a function that takes an array of numbers and returns an array of numbers of the same length.
Each element of the output array out[i] should be equal to the product of all of the elements of the input array
except for in [i].
"""

# Example:

# input_ = [1, 2, 3, 4]
# output_ = [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3] = [24, 12, 8, 6]

# in = [1, 2, 0, 4]

import math


# from time import time
# from itertools import combinations


# Does not work in leetcode
def product_with_zero(arr):
    result = [0] * len(arr)
    zero_count = arr.count(0)
    if not zero_count:
        for i in range(len(arr)):
            result[i] = math.prod(arr) // arr[i]

    elif zero_count == 1:
        new_arr, zero_idx = list(arr), arr.index(0)
        del new_arr[zero_idx]
        result[zero_idx] = math.prod(new_arr)

    return result


# My original solution
def product_with_zero(nums):
    def prod(arr):
        prod, zero_idx = 1, []
        for i in range(len(arr)):
            if arr[i] != 0:
                prod *= arr[i]
            else:
                zero_idx.append(i)
                if len(zero_idx) == 2:
                    break
        return prod, zero_idx

    result = [0] * len(nums)
    myprod, zero_idx = prod(nums)  # pylint: disable=invalid-name
    if not zero_idx:
        for i in range(len(nums)):
            result[i] = myprod // nums[i]

    elif len(zero_idx) == 1:
        result[zero_idx[0]] = myprod

    return result


# Neet code solution
def product_with_zero_2(nums):
    prod, zero_cnt = 1, 0
    for num in nums:
        if num:
            prod *= num
        else:
            zero_cnt += 1
    if zero_cnt > 1:
        return [0] * len(nums)

    res = [0] * len(nums)
    for i, c in enumerate(nums):
        if zero_cnt:
            res[i] = 0 if c else prod
        else:
            res[i] = prod // c
    return res


# Brute force one by one
def product_Onˆ2_v1(arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if arr[i] != arr[j]:
                prod *= arr[j]
        result[i] = prod

    return result


# Brute force suing array slices
def product_Onˆ2_v2(arr):
    result = []
    for i in range(len(arr) - 1):
        cur_arr = arr[:i] + arr[i + 1:]
        result.append(math.prod(cur_arr))
    result.append(math.prod(arr[:-1]))

    return result
    # return list(map(lambda x: math.prod(x), combinations(reversed(mylist), len(mylist) - 1))) # Inefficient


# Solution without input that does not include zeros
def product_On(arr):
    result = []
    prod = math.prod(arr)
    for i in range(len(arr)):
        result.append(prod / arr[i])

    return result


# seqs = [[1, 2, 3, 4], [-1, 1, 0, -3, 3], [0, 0, 2, 4, 5]]
# for s in seqs:
# s = [1, 2, 0, 6]
# print(product_with_zero_2(s))

print(product_Onˆ2_v1([1, 2, 3, 4]))

# mylist = list(range(1, 21))
#
# result = []
# start = time()
# product_Onˆ2(mylist)
# result.append(time() - start)
# print(result[0])
# start = time()
# myproduct_On(mylist)
# result.append(time() - start)
# print(result[1])
# start = time()
# product_with_zero(mylist)
# result.append(time() - start)
# print(result[2])
# start = time()
# list(map(lambda x: math.prod(x), combinations(mylist, len(mylist) - 1)))
# result.append(time() - start)
# print(result[3])
#
# print(result)
# print(sorted(result))
