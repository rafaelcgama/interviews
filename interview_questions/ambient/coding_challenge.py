# Given a list of files in a file system, print them with identation,
# for each directory - First non-repeated char in a word


from collections import Counter
from typing import Optional
import hashlib
import os


# Finds the first non-repeated character in a string
def first_non_repeated(word):
    counts = Counter(word)
    for c in word:
        if counts[c] == 1:
            return c
    return "-"


# Inserts each file path into a nested dictionary tree
def create_tree(tree, path):
    curr = tree
    path_list = path.split('/')
    for part in path_list:
        curr = curr.setdefault(part, {})


# Recursively prints the tree with indentation and FNR char
def print_tree(tree, indent=0):
    for name in sorted(tree.keys()):
        fnr = first_non_repeated(name)
        print("  " * indent + f"{name} (first non-repeated: {fnr})")
        print_tree(tree[name], indent + 1)


# Example file list
paths = [
    "root/folder1/fileA.txt",
    "root/folder1/fileB.txt",
    "root/folder2/fileC.txt",
    "root/folder2/subfolder/fileD.txt"
]


# # Build the tree
# tree = {}
# for path in paths:
#     create_tree(tree, path)
#
# # Print the result
# print_tree(tree)

def compute_hash(filepath: str) -> str:
    hash = hashlib.sha1()
    with open(filepath, "rb") as f:
        file = f.read()
        hash.update(file)
    return hash.hexdigest()


def search_for_hash(start_dir: str, hash_value: str) -> Optional[dict]:
    """
        start_dir: str starting directory of where to begin search
        hash_value: str sha1 hash of what you are looking for in start_dir

        :returns: dictionary with the name, path, and hash of the file if found or None if not
        {
            "name": "nope.py",
            "path": "start/sub-1/nope.py",
            "hash": "a0b8c2cdf1b52e7d65
        :returns: dictionary with the name, path, and hash of the file if found or None if not

        Use docs.python.org for documentation
    """

    # dir_list = os.listdir(start_dir)
    # for value in dir_list:
    #     path = os.path.join(start_dir, value)
    #     if os.path.isdir(path):
    #         result = search_for_hash(path, hash_value)
    #         if result:
    #             return result
    #
    #     elif os.path.isfile(path):
    #         file_hash = compute_hash(path)
    #         if file_hash == hash_value:
    #             return {
    #                 "name": value,
    #                 "path": path,
    #                 "hash": hash_value
    #             }

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = compute_hash(filepath)

            if file_hash == hash_value:
                return {
                    "name": file,
                    "path": filepath,
                    "hash": hash_value
                }

def walk_through_folder(start_dir):
    for root, dirs, files in os.walk(start_dir):
        print(root)
        for f in files:
            print(f"{os.path.join(root, f)}")


#TODO:
# Add cache to improve
# Add try/except arguments
if __name__ == "__main__":
# result = search_for_hash('start', 'a0b8c2cdf1b52e7d65f23e5387dcd35327a97445')
# print("RESULT\n==================================")
# print(result)
#     print(search_for_hash('start', 'da39a3ee5e6b4b0d3255bfef95601890afd80709'))
    walk_through_folder("start")