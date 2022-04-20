from collections import deque, Counter
from typing import Any, Dict


def is_anagram(s1: str, s2: str):
    '''Is s1 an anagram of s2?'''
    return Counter(s1) == Counter(s2)


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


assert is_anagram_substr('car', 'erca'), "Not anagram substring"
assert not is_anagram_substr('rats', 'rates'), "It is anagram substring"


def flatten(obj: Dict[str, Any]):
    # Flatten a JSON object
    output = {}

    def dfs(item, name=[]):
        if isinstance(item, dict):
            for key in item:
                dfs(item[key], name=(name + [key]))
        else:
            output[".".join(name)] = item

    dfs(obj)

    return output


def flatten_bfs(obj):
    output = {}

    queue = deque([(obj, "")])
    while queue:
        cur_obj, name = queue.popleft()
        if len(cur_obj):
            for key in cur_obj:
                if isinstance(cur_obj[key], dict):
                    queue.append((cur_obj[key], f"{name}{key}."))

                else:
                    output[f"{name}{key}"] = cur_obj[key]

    return output


obj1 = {
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
}

obj2 = {
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
}
from time import time

start = time()
flatten(obj1)
diff1 = time() - start
print(diff1)
start = time()
flatten_bfs(obj1)
diff2 = time() - start
print(diff2)

print((diff2 - diff1) / diff1)

assert flatten(obj1) == {'a': 1, 'c.a': 2, 'c.b.x': 5, 'c.b.y': 10, 'd': [1, 2, 3]}, "Result wasn't flattened correctly"

assert flatten(obj2) == {'a': 1, 'c.a': 2, 'c.b.x.r': 2, 'c.b.x.s': 4, 'c.b.y': 10,
                         'd': [1, 2, 3]}, "Result wasn't flattened correctly"
