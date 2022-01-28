from collections import Counter


### INUIT ###

def find_nodes_zero_one_parents(pairs):
    parents = []
    children = []
    for pair in pairs:
        parents.append(pair[0])
        children.append(pair[1])

    zero_parent = list(set(parents) - set(children))

    one_parent = Counter(children)
    one_parent = [key for key, value in one_parent.items() if value == 1]

    return [zero_parent, one_parent]  # Does it have to be sorted?


if __name__ == '__main__':
    parent_child_pairs = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [8, 10]
    ]

    find_nodes_zero_one_parents(parent_child_pairs)
