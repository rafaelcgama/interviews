# We want to build a stack
# We want other developers to use our stack
# We cant use any built in data structures no tuple, no list, no dictionary

class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


class Stack:
    def __init__(self):
        self.stack = None

    def pop(self):
        val = self.stack.val
        self.stack = self.stack.next
        return val

    def push(self, val):
        self.stack = Node(val, self.stack)

    def is_empty(self):
        return True if self.stack is None else False
