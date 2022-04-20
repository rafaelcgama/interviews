# DFS recursive
def dfs(tree):
    if tree is not None:
        print(tree)
        dfs(tree.left)
        dfs(tree.right)


# DFS interactive
def dfs(tree, stack):
    stack.append(tree)
    while len(stack):
        node = stack.pop()
        if node:
            print(node)
            stack.append(node.left)
            stack.append(node.right)


# Binary Search
def binary_search(mylist, target):
    left, right = 0, len(mylist) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mylist[mid] == target:
            return mid

        elif mylist[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1
