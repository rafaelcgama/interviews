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


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class ListNode:
    def __init__(self, item=None, next_=None, random_=None):
        self.item = item
        self.next = next_
        self.random = random_

    def create_linked_list(self, mylist):
        head = tail = ListNode()
        for item in mylist:
            tail.next = ListNode(item=item)
            tail = tail.next

        return head.next

    def print_linked_list(self, head):
        tail = head
        while tail:
            print(tail.item)
            tail = tail.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_from_list(self, elements):
        root_node = TreeNode(val=elements[0])
        nodes = [root_node]
        for i, x in enumerate(elements[1:]):
            if x is None:
                continue
            parent_node = nodes[i // 2]
            is_left = (i % 2 == 0)
            node = TreeNode(val=x)
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node
            nodes.append(node)

        return root_node


class Solution:

    def championship(self, races, points):
        racer_points = defaultdict(int)
        for x, race in enumerate(races):
            print(f"race {x + 1}")
            print("rider           points")
            print("-----------------------")
            for i, racer in enumerate(race):
                if i == 0:
                    racer_points[racer] += points[i]
                elif i == 1:
                    racer_points[racer] += points[i]

                elif i == 2:
                    racer_points[racer] += points[i]

                else:
                    racer_points[racer] += 0

            for x, y in Counter(racer_points).most_common():
                print(x + "----------" + str(y))
            print("")

if __name__ == "__main__":
    x = Solution()
    races = [
        ["lorenzo", "hayden", "dovizioso", "rossi", "marquez"],
        ["marquez", "hayden", "rossi", "dovizioso", "lorenzo"],
        ["rossi", "lorenzo", "dovizioso", "hayden", "marquez"],
        ["dovizioso", "marquez", "rossi", "lorenzo", "hayden"],
        ["marquez", "dovizioso", "rossi", "lorenzo", "hayden"],
        ["marquez", "dovizioso", "hayden", "rossi", "lorenzo"],
        ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"],
        ["marquez", "rossi", "lorenzo", "hayden", "dovizioso"],
        ["lorenzo", "marquez", "rossi", "dovizioso", "hayden"],
        ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"]
    ]

    points = {
        0: 15,
        1: 10,
        2: 5
    }
    x.championship(races, points)


