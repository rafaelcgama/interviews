from leet_code import ListNode, TreeNode


#### RECURSIVE FUNCTIONS ####

### STRINGS ###
def reverse_string(mystring):
    if not mystring:
        return ""

    return reverse_string(mystring[1:]) + mystring[0]


def is_palindrome(mystring):
    if 0 <= len(mystring) <= 1:
        return True

    if mystring[0] == mystring[len(mystring) - 1]:
        return is_palindrome(mystring[1: len(mystring) - 1])

    return False


### NUMBERS ###
def decimal_to_binary(number, result):
    if not number:
        return result

    result = str(number % 2) + result

    return decimal_to_binary(number // 2, result)


def recursiveSummation(number):
    if number <= 1:
        return number

    return number + recursiveSummation(number - 1)


### DIVIDE AND CONQUER ###

## BINARY SEARCH ##
def binary_search(A, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if target == A[mid]:
        return mid

    if target < A[mid]:
        return binary_search(A, left, mid - 1, target)

    return binary_search(A, mid + 1, right, target)


## FIBONACCI (Non-Optimized) ##
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


cache = {0: 1, 1: 1}


def fibonnaci_memoization(n):
    cache = {0: 1, 1: 1}

    def fib(n):
        if n in cache:
            return cache[n]

        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

    return fib(n)

## MERGE SORT ##


## LINKED LIST REVERSAL ##'
def reverse_linked_list(head):
    if not head or not head.next:
        return head

    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return p


def sorted_merge(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.item < l2.item:
        l1.next = sorted_merge(l1.next, l2)
        return l1
    else:
        l2.next = sorted_merge(l1, l2.next)
        return l2


### TREE ###
# Insert value into Binary Search Tree (BST)
def insert_node(head, value):
    if not head:
        head = TreeNode(val=value)
        return head

    if head.val > value:
        head.left = insert_node(head.left, value)
    else:
        head.right = insert_node(head.right, value)

    return head


def print_tree(head):
    if head:
        print_tree(head.left)
        if head.val == 150:
            print('stop')
        print(head.val)
        print_tree(head.right)


### Graphs ###
# Find a node in a graph using DFS
def dfs(node, visited, target):
    if not node:
        return False

    if node.val == target:
        return True

    for neighbor in node.get_neighbors():
        if neighbor in visited:
            continue

        visited.append(neighbor)
        is_found = dfs(neighbor, visited, target)

        if is_found:
            return True

    return False


if __name__ == "__main__":
    linked_list = ListNode()
    # l1 = linked_list.create_linked_list([2, 5, 8])
    # l2 = linked_list.create_linked_list([1, 3, 4, 6, 8])
    # merged_linked_list = sorted_merge(l1, l2)
    # linked_list.print_linked_list(merged_linked_list)

    # mylist = [100, 80, 50, 90, 30, 60, 90, 85, 95, 120, 110, 108, 115, 140, 150]
    # root = None
    # for num in mylist:
    #     root = insert_node(root, num)
    #
    # print_tree(root)

print(fibonacci(4))
