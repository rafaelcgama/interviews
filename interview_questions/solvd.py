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


"""
without using a JSON library, print the JSON string representation of the input python object, Test cases ignore 
whitespace and array ordering

for reference therese are all the valid JSON data type:
- JSON object (key-value pair with string keys)
- array
- string
- number
- boolean
-null

input : a python object
output: the json string representation of the object
"""


def json_stringify(obj):
    # Helper function to handle each data type recursively
    def json_str_obj(element):
        if isinstance(element, dict):  # JSON object
            pairs = []
            for key, value in sorted(element.items()):  # Sort keys to ignore ordering
                pairs.append(f'"{key}":{json_str_obj(value)}')
            return "{" + ",".join(pairs) + "}"

        elif isinstance(element, list):  # Array
            elements = [json_str_obj(item) for item in element]
            return "[" + ",".join(elements) + "]"

        elif isinstance(element, str):  # String
            return f'"{element}"'

        elif isinstance(element, (int, float)):  # Number (integer or float)
            return str(element)

        elif isinstance(element, bool):  # Boolean
            return str(element).lower()

        elif element is None:  # Null
            return "null"

    return json_str_obj(obj)

"""
implement the "find_smallest_interval(numbers)" function which return the smallest positive interval between two values 
of the numbers list
"""
def find_smallest_interval(numbers):
    # Step 1: Sort the numbers list in ascending order
    numbers.sort()

    smallest_interval = float('inf')
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if 0 < diff < smallest_interval:
            smallest_interval = diff

    return smallest_interval

"""
we call a integer a "duodigit" if its decimal representation uses no more than two different digits. For example, 12, 
110, -33333 are duodigits, but 102 is not

implement the function is_duo_digit(number which returns a string )
"""

def is_duo_digit(number):
    myset = set()
    number = abs(number)
    while number:
        myset.add(number % 10)
        number //= 10

    return "y" if myset <= 2 else "n"