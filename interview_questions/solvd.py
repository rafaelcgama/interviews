"""
Implement a function that takes in a list of strings
and returns a list of all the string pairs that are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

For example, given the list ["listen", "silent", "google", "ooggle", "hell", "hello"],
the function should return [["listen", "silent"], ["google", "ooggle"]].


Test case: ["listen", "silent", "google", "ooggle", "hell", "hello", "enlist"]
Expected output: [["listen", "silent", “enlist”], ["google", "ooggle"]]

Test case: ["listen", "ooggle", "hell", "hello" ]
Expected output: []
"""

from collections import defaultdict
from typing import List
import unittest
from datetime import timedelta


def group_anagrams(mylist: List[str]) -> List[List[str]]:
    ## O(logn)
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


def json_stringify(element):
    # Helper function to handle each data type recursively
    if isinstance(element, dict):  # JSON object
        pairs = []
        for key, value in element.items():
            pairs.append(f'"{key}": {json_stringify(value)}')
        return "{" + ",".join(pairs) + "}"

    elif isinstance(element, list):  # List
        elements = [json_stringify(item) for item in element]
        return "[" + ",".join(elements) + "]"

    elif isinstance(element, str):  # String
        return f'"{element}"'

    elif isinstance(element, (int, float)):  # Number (integer or float)
        return str(element)

    elif isinstance(element, bool):  # Boolean
        return str(element).lower()

    elif element is None:  # Null
        return "null"


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
we call a integer a "duo-digit" if its decimal representation uses no more than two different digits. For example, 12, 
110, -33333 are duo-digits, but 102 is not. 
Implement the function is_duo_digit(number which returns a string )
"""


def is_duo_digit(number):
    myset = set()
    number = abs(number)
    while number:
        myset.add(number % 10)
        number //= 10

    return "y" if len(myset) <= 2 else "n"


# write the body of the next_week(d) func that return date 7 days after the date given output
def next_week(d):
    return d + timedelta(days=7)

# Given the following code
class A:
    custom_prop = []

    def __init__(self, value=None):
        if value:
            self.custom_prop.append(value)

a = A(10)
b = A()
print(b.custom_prop)


class A:
    def test(self):
        print('A')

class B(A):
    def test(self):
        super().test()
        print('B')

class C(A):
    def test(self):
        print("C")

class D(B, C):
    def test(self):
        super().test()
        print("D")

d = D()
print(d.test())

# Write the body of the function "is_on_even_position(table, value)". The function should return True if value
# is contained in table at an even index, False otherwise
def is_on_even_position(table, value):
    position = table.index(value)
    if not position % 2:
        return True
    return False

"""
Implement the function "encode(plain_text) which returns an encoded message. 
It receives a "plain_text" string parameter, for example, "aaaabcccaaa"
You myst encode it by countng each consecutive sequence of a letter. e.g. in "aaaabcccaaa" there are:

* 4 times the letter "a"
* then 1 "b"
* then 3 "c"
* then 3 "a" 

Therefore you must return the string 4a1b3c3a

Constrains:
* plain_text is made of lowercase letter: a-z
* plaint_text is never None and has a maximum length of 15000 characters

Example:
PlainText      EncodedText 
aabaa          2a1b2a

PlainText      EncodedText 
aaaabcccaaa    4a1b3c3a
"""

def encode(plain_text):
    encoded_text = ""
    current_char = plain_text[0]
    count = 1
    for i in range(1, len(plain_text)):
        if plain_text[i] == current_char:
            count += 1
        else:
            encoded_text += f"{count}{current_char}"
            current_char = plain_text[i]
            count = 1
    encoded_text += f"{count}{current_char}"
    return encoded_text
