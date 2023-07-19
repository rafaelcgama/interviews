"""
Implement a function that takes in a list of strings
and returns a list of all the string pairs that are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

For example, given the list ["listen", "silent", "google", "ooggle", "hell", "hello"],
the function should return [["listen", "silent"], ["google", "ooggle"]].


Test case:  ["listen", "silent", "google", "ooggle", "hell", "hello", "enlist"]
Expected output: [["listen", "silent", “enlist”], ["google", "ooggle"]]

Test case:  ["listen", "ooggle", "hell", "hello" ]
Expected output: []
"""

from collections import defaultdict
from typing import List


def group_anagrams(mylist: List[str]) -> List[List[str]]:
    # # O nlogn because of the sorted function
    # res = defaultdict(list)
    # for s in mylist:
    #     key = "".join(sorted(s))
    #     res[key].append(s)
    # return [v for v in res.values() if len(v) > 1]

    # O (m x n) m (number of strings) and n (number of chars in each string)
    res = defaultdict(list)

    for s in mylist:

        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)

    return [v for v in res.values() if len(v) > 1]


import unittest


class MyTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(group_anagrams(["listen", "silent", "google", "ooggle", "hell", "hello"]),
                         [["listen", "silent"], ["google", "ooggle"]])

    def test2(self):
        self.assertEqual(group_anagrams(["listen", "silent", "google", "ooggle", "hell", "hello", "enlist"]),
                         [["listen", "silent", "enlist"], ["google", "ooggle"]])

    def test3(self):
        self.assertEqual(group_anagrams(["listen", "ooggle", "hell", "hello"]), [])
