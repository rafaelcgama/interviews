from collections import Counter


def is_anagram(s1: str, s2: str):
    '''Is s1 an anagram of s2?'''
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    return counter1 == counter2


def is_anagram_substr(needle: str, haystack: str):
    '''
    Is there an anagram of needle that is a substring of haystack?
    '''
    len_needle = len(needle)
    len_haystack = len(haystack)

    for i in range(len_haystack - len_needle + 1):
        if is_anagram(haystack[i:i + len_needle], needle):
            return True
    return False


assert is_anagram_substr('car', 'erca') == True, "Not anagram substring"
assert is_anagram_substr('rats', 'rates') == False, "It is anagram substring"

from typing import Any, Dict


def flatten(obj: Dict[str, Any]):
    '''
    Flatten a JSON object
    '''
    output = {}

    def dfs(item, name=[]):
        if isinstance(item, dict):
            for key in item:
                dfs(item[key], name=name + [key])
        else:
            output[".".join(name)] = item

    dfs(obj)

    return output


assert flatten(
    {
        "a": 1,
        "c": {
            "a": 2,
            "b": {
                "x": 5,
                "y": 10
            }
        },
        "d": [
            1,
            2,
            3
        ]
    }) == {'a': 1, 'c.a': 2, 'c.b.x': 5, 'c.b.y': 10, 'd': [1, 2, 3]}, "Result wasn't flattened correctly"

assert flatten(
    {
        'a': 1,
        'c': {
            'a': 2,
            'b': {
                'x': {
                    'r': 2,
                    's': 4
                },
                'y': 10
            }
        },
        'd': [
            1,
            2,
            3
        ]
    }) == {'a': 1, 'c.a': 2, 'c.b.x.r': 2, 'c.b.x.s': 4, 'c.b.y': 10,
           'd': [1, 2, 3]}, "Result wasn't flattened correctly"
