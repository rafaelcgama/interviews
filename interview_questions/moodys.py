'''
1. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. (Try not to use built in functions)
'''


class Stack:
    def __init__(self):
        self.stack = []
        self.min_ = None

    def push(self, num):
        self.min_ = self.min_ if self.min_ else num
        self.min_ = min(self.min_, num)
        self.stack.append(num)

    def pop(self):
        value = self.stack[-1]
        self.min_ = min(value, self.min_)
        self.stack = self.stack[:-1]
        return value

    def top(self):
        print(self.stack[-1])

    def retrieve(self):
        return self.min_


def climbStairs(n: int) -> int:
    # Dynamic Programming
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
