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


## Arrays & Hashing

class Solution:

    # 217. Contains Duplicate
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

    # 242. Valid Anagram
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

    # 1. Two Sum
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

    # 49. Group Anagrams
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
        # return [mydict[k] for k in mydict]

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

    # 347. Top K Frequent Elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        Easiest way is to count the elements, sort (most_common function) and return the k most common.
        """
        # return [c[0] for c in Counter(nums).most_common(k)]

        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        First we count the elements in a dict and create a list of empty lists that match the size of "nums". This is 
        done in case each element one appears once. Then we iterate through the count dict and use the count to select 
        nums[count] and append the number in the list. This way every time a number appears with the same count it will
        be appended in the list in nums[count].
        Finally, since the elements with most occurrences will be on the right of the list, we need to interate the 
        freq list in reverse and iterate the list in each freq[i] for get the elements from each one and stopping the
        iteration when the "k" were collected
        """
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i, _ in reversed(list(enumerate(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    s = Solution()

    print(s.groupAnagrams())
