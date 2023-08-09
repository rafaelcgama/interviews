import copy
import math
import json
import heapq
import bisect
import collections
from typing import *
from copy import deepcopy
from functools import cache
from itertools import groupby
# from drawtree import draw_level_order  # '{2,#,3,#,4,#,5,#,6}')
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, accumulate, product
import operator


### NEATCODE ROADMAP (https://neetcode.io/roadmap) ###

# TODO ## Arrays & Hashing ##

class Solution:

    # 217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Create a set from the list and compare the length of the two but the following way is better because
        it doesn't have to iterate through the entire list to create the set. It increases as the list iteration
        goes it stops if a duplicate is found earlier making it more performative.
        """
        myset = set()

        for n in nums:
            if n in myset:
                return True
            myset.add(n)
        return False

    # 242. Valid Anagram (https://leetcode.com/problems/valid-anagram/)
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Count the occurrences of each letter in the string and compare them. If the count matches, it is an anagram.
        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

    # 1. Two Sum (https://leetcode.com/problems/two-sum/)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        In order to achieve a O(n) solution the difference between the target and the nth number in the list is
        being stored in dictionary with its respective index as a value in case it hasn't been inserted yet. If it has,
        the index can be retrieved and used to build the solution.
        """
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [i, prev_map[diff]]
            prev_map[diff] = i

    # 49. Group Anagrams (https://leetcode.com/problems/group-anagrams/)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """

        # mydict = {}
        #
        # for s in strs:
        #     key = "".join(sorted(s))
        #     mydict[key] = mydict.get(key, list()) + [s]
        #
        # return mydict.values()

        """
        Time complexity: O(m x n)
        Space complexity: O(n)
        Create a list with the number of alphabet chars (26 since they are all lower case) and use the ord(n) - ord("a")
        trick to select the equivalent position in the list to count how many times each char appears. Then convert the
        list to tuple so it can be used as a key in the mapping dict and append the word being analyzed so a list of
        words can be created for each count. 
        """
        mydict = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            mydict[tuple(count)].append(s)

        return mydict.values()

    # 347. Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        Easiest way is to count the elements, sort (most_common function) and return the k most common.
        """
        # return Counter(nums).most_common(k).values()
        """
        Time complexity: O(m x n) 
        Space complexity: O(n)
        """
        # First we count the elements in a dict
        count = Counter(nums)
        # This list needs to be created with + 1 in case so there is no idx problem in case there is only one number
        # in nums.
        freq = [[] for _ in range(len(nums) + 1)]

        # Now we use the count as an index to fill the freq list. This is done to make sure that the numbers with the
        # highest count are in the rightmost portion of the list, so we can iterate it in reverse in the next step
        # to find out the most common numbers.
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Now we iterate the freq list in reverse and iterate the list in each index. The iteration will stop when res
        # has the size of k
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # 238. Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Ex. [1, 2, 3, 4]
        In order to know the product of the array except itself, it is necessary to calculate the product of the
        numbers that come before i (prefix) and of those that come after(postfix).
        So we create a list that multiplies its element in increasing order which will result in [1, 2, 6, 12] and do
        the same in inverse order resulting [24, 24, 12, 4]
        Finally, we would use the calculation in line 160 to multiply the prefix number before i and the postfix number
        after i.
        To facilitate we can input the first and last elements of the result list beforehand as they are predictable.
        """
        # prefix = list(accumulate(nums, func=operator.mul))
        # postfix = list(reversed(list(accumulate(reversed(nums), func=operator.mul))))
        #
        # result = [postfix[1]] + ([0] * (len(nums) - 2)) + [prefix[len(nums) - 2]]
        #
        # for i in range(1, len(nums) - 1):
        #     result[i] = prefix[i - 1] * postfix[i + 1]
        #
        # return result

        """
        Time complexity: O(n)
        Space complexity: O(n) in the context of the problem
        This version is slightly more performative because, as per problem's conditions, the "res" list is not 
        considered extra memory and we don't use waste runtime and extra memory calculating prefix/postfix as they 
        are calculated in loops in O(1) time and using O(1) memory.
        First a result array is created and having the same size as nums and populated by "1"s.
        Then we set prefix/postfix to 1 to aid in their calculations as because nums[0] will go to result[1] and that's
        when the accumulation starts. The same is true in descending order but since the the prefix is already in result
        nums[-1] will multiply nums[-1] 
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    # 36. Valid Sudoku (https://leetcode.com/problems/valid-sudoku/)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time complexity: O(nˆ2)
        Space complexity: O(n)
        # According to the rules a number can't appear more than 1 in any row, col or quadrant.
        Default dict of set are created to store and verify numbers
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Loop through the board
        for r in range(9):
            for c in range(9):
                # Ignore "." occurrences
                if board[r][c] == ".":
                    continue

                # Check if board element is already in row, column or quadrant. If so, return False
                elif board[r][c] in rows[r] or \
                        board[r][c] in cols[c] or \
                        board[r][c] in squares[(r // 3, c // 3)]:  # r // 3 because each quadrant is made of 3x3
                    return False

                else:
                    # Insert in the dictionaries in case the number obeys the above condition
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])

        return True

    # 659 · Encode and Decode Strings (ttps://www.lintcode.com/problem/659/)
    def encode(words: List[List[str]]):
        result = ''
        for word in words:
            result += (chr(len(word)) + word)
        return result

    def decode(self, encoded: str) -> List:
        result = []
        i = 0

        while i < len(encoded):
            word_len = ord(encoded[i])
            i += 1

            word = encoded[i: i + word_len]
            result.append(word)

            i += word_len

        return result

    # 128. Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence/)
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The trick here is to first convert the list into a set for 2 reasons.
        First: it will eliminate duplicates
        Second: checking in a set is a O(1) operation whereas in a list is O(n). Then we create variable to keep track
        of the max_len
        """
        nums_set, max_len = set(nums), 0

        for num in nums:
            # Check if a number has a preceding number in list. If it has that means that it is not the beginning of
            # a sequence and rather the continuation of one. So we keep iterating number we find that number and start
            # or not the counting of a sequence or not for the same reason.
            if (num - 1) not in nums_set:
                cur_len = 0
                # Start counting how many sequential numbers are there
                while (num + cur_len) in nums_set:
                    cur_len += 1
                max_len = max(max_len, cur_len)

        return max_len

    # TODO ## Two Pointers ##
    # 125. Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alphanumeric function
    def alphanum(self, c):
        return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
        )

    # 167. Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

    # 15. 3Sum (https://leetcode.com/problems/3sum/)
    def threeSum(self, nums: List[int]) -> List[int]:
        """
        The easiest solution and most inefficient is a triple nested loop O(nˆ3).
        Time complexity: O(nˆ2)
        Space complexity: O(1)
        """
        res = []
        # We need to sort to avoid using the same numbers to achieve the same solution as you would in a triple nested
        # loop and to make the runtime more efficient
        nums.sort()

        for i, a in enumerate(nums):
            # This is done to avoid using a number that was previously used and the i > 0 is to make sure this condition
            # only happens after the first number of the array is used
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1  # It is necessary to update the left point here so the loop in line 326 continues
                    # This is necessary for the same reason as in line 319. To avoid repeated solutions
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            return res

    # 11. Container With Most Water (https://leetcode.com/problems/container-with-most-water/)
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height) - 1

        while l < r:
            res = max(min(height[l], height[r]) * (r - l), res)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res

    # TODO ## Stack ##
    # 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
    def isValid(self, s: str) -> bool:
        mymap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for c in s:
            if c not in mymap:
                stack.append(c)
            if not stack or stack[-1] != mymap[c]:
                return False
            stack.pop()
        return not stack

    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            val = min(val, self.min_stack[-1] if self.min_stack else val)
            self.min_stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

    # 150. Evaluate Reverse Polish Notation (https://leetcode.com/problems/evaluate-reverse-polish-notation/)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))

        return stack[0]

    # 22. Generate Parentheses (https://leetcode.com/problems/generate-parentheses/)
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IF open == closed == n

        stack, res = [], []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res

    # 739. Daily Temperatures (https://leetcode.com/problems/daily-temperatures/)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n)
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                answer[stack_idx] = (i - stack_idx)
            stack.append((t, i))

        return answer

    # 853. Car Fleet (https://leetcode.com/problems/car-fleet/)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = list(zip(position, speed))  # Join both for practicality
        p_s.sort(key=lambda x: x[0])

        stack = []
        for p, s in reversed(p_s):
            eta = (target - p) / s
            stack.append(eta)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    # 704. Binary Search (https://leetcode.com/problems/binary-search/)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return -1

    # 74. Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        row, top, bot = 0, 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        else:
            return False

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
