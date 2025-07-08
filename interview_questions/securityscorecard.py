"""
Write a function or method that takes 2 strings as inputs and returns a boolean specifying whether the strings are anagrams of each other.

Strings are anagrams of each other if they contain the same characters. The order of the characters is insignificant.

Examples:
“aabc”, “baca” -> true
“aabc”, “bbca” -> false
"""


# If you want to create your own counter
def counter(s):
    mydict = {}
    for c in s:
        mydict[c] = mydict.get(c, 0) + 1
    return mydict


from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """
    Time complexity: O(n) because it is O(2n) but the constant is eliminated
    Space complexity: O(1) because the alphabet letters are fixed
    """
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


"""
Write a function or method that takes 2 strings as inputs and returns a boolean specifying whether a substring of the first string is an anagram of the second.

Examples:

“aaaaaabacbaaa”, “baca” -> true
“aaaabaaaaacaa”, “baca” -> false
"""


def is_substring_anagram(s: str, s_sub: str) -> bool:
    """
    Time complexity: O(n) It iterates "s" but since the c1 in each iteration is fixed, it becomes O(1)
    Space complexity: O(1) because the alphabet only has 26 characters, this is as big as the counter will get it can be
                      considered constant time.
    """
    if len(s_sub) > len(s):  # if the substring is longer than the string, the problem makes no sense
        return False

    counter2, l, r = Counter(s_sub), 0, len(s)

    while r <= len(s):
        counter1 = Counter(s[l:r])
        if counter1 == counter2:
            return True
        l += 1
        r += 1

    return False


print(is_substring_anagram("aaaabaaaaacaa", "baca"))
