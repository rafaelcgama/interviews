# import copy
# import math
# import json
# import heapq
# import bisect
# import collections
# from typing import *
# from copy import deepcopy
# from functools import cache
# from itertools import groupby
# # from drawtree import draw_level_order  # '{2,#,3,#,4,#,5,#,6}')
# from collections import deque, Counter, defaultdict
# from itertools import permutations, combinations, accumulate, product
# import operator
#
#
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
#
#
# class ListNode:
#     def __init__(self, item=None, next_=None, random_=None):
#         self.item = item
#         self.next = next_
#         self.random = random_
#
#     def create_linked_list(self, mylist):
#         head = tail = ListNode()
#         for item in mylist:
#             tail.next = ListNode(item=item)
#             tail = tail.next
#
#         return head.next
#
#     def print_linked_list(self, head):
#         tail = head
#         while tail:
#             print(tail.item)
#             tail = tail.next
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#     def create_from_list(self, elements):
#         root_node = TreeNode(val=elements[0])
#         nodes = [root_node]
#         for i, x in enumerate(elements[1:]):
#             if x is None:
#                 continue
#             parent_node = nodes[i // 2]
#             is_left = (i % 2 == 0)
#             node = TreeNode(val=x)
#             if is_left:
#                 parent_node.left = node
#             else:
#                 parent_node.right = node
#             nodes.append(node)
#
#         return root_node
#
#
# def parse_config(path: str) -> dict:
#     """
#     Parses an INI configuration file and returns the configuration data as a dictionary.
#     """
#     config = {}
#     section = None
#
#     with open(path, 'r') as f:
#         for line in f:
#             line = line.strip()
#
#             # Skip comments and blank lines
#             if not line or line.startswith(';'):
#                 continue
#
#             # Check for section headers
#             if line.startswith('[') and line.endswith(']'):
#                 section = line[1:-1]
#                 config[section] = {}
#             else:
#                 # Parse key-value pairs
#                 key, value = line.split('=', maxsplit=1)
#                 key = key.strip()
#                 value = value.strip()
#
#                 # Convert value to appropriate type
#                 if value.isdigit() or value[1:].isdigit():
#                     value = int(value)
#                 elif value.replace('.', '', 1).isdigit():
#                     value = float(value)
#                 elif value.lower() == 'yes' or value.lower() == 'true' or value.lower() == 'on':
#                     value = True
#                 elif value.lower() == 'false' or value.lower() == 'off':
#                     value = False
#
#                 config[section][key] = value
#
#     return config
#
#
# output = parse_config("interview_questions/cash_app/generic.ini")
#
# expected = {
#     "section": {
#         "b": False,
#         "f": 206.201,
#         "i": -55,
#         "i1": 1,
#         "b1": True,
#         "b2": False,
#         "s": "",
#     },
# }
#
# assert output == expected
#
from typing import List

#
#
# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     res = [0] * n
#     pref = [0] * n
#     suff = [0] * n
#
#     pref[0] = suff[n - 1] = 1
#     for i in range(1, n):
#         pref[i] = nums[i - 1] * pref[i - 1]
#
#     for i in range(n - 2, -1, -1):
#         suff[i] = nums[i + 1] * suff[i + 1]
#
#     for i in range(n):
#         res[i] = pref[i] * suff[i]
#
#     return res
#
#
# nums = [1, 2, 3, 4]
#
# print(productExceptSelf(nums))

# def min_stack(s):
#     class MinStack:
#         def __init__(self):
#             self.stack = []
#             self.min = []
#
#         def push(self, value):
#             self.stack.append(value)
#             if not self.min:
#                 self.min.append(value)
#             else:
#                 self.min.append(min(self.min[-1], value))
#
#         def pop(self):
#             self.stack.pop()
#             self.min.pop()
#
#         def top(self):
#             return self.stack[-1]
#
#         def get_min(self):
#             return self.min[-1]

