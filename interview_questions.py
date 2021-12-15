import unittest
from collections import Counter


### GOOGLE ###
# sentence = 'sixixi'
# list_words = ['s', 'si', 'sixi', 'ix', 'xi']

def remove_word(word, sentence, mylist):
    while sentence.find(word) >= 0:
        idx = sentence.find(word)
        sentence = sentence[: idx] + sentence[idx + len(word):]
        mylist.append(word)

    return sentence


def max_len_combination(sentence, list_words):
    mylist = []
    mydict = {}
    for i in range(len(list_words)):
        new_word = remove_word(list_words[i], sentence, mylist)
        for j in range(i + 1, len(list_words)):
            new_word = remove_word(list_words[j], new_word, mylist)

        if not new_word:
            mydict[len(mylist)] = list(mylist)

        mylist = []

    return sorted(mydict[max(mydict.keys())])


class TestSmallestLetter(unittest.TestCase):

    def test_1(self):
        sentence = 'barfoobar'
        list_words = ['bar', 'foo']
        result = ['bar', 'foo', 'bar']
        self.assertEqual(max_len_combination(sentence, list_words), sorted(result))

    def test_2(self):
        sentence = 'tomorrow'
        list_words = ['to', 'tom', 'morrow', 'or', 'row']
        result = ['tom', 'or', 'row']
        self.assertEqual(max_len_combination(sentence, list_words), sorted(result))

    def test_3(self):
        sentence = 'abcd'
        list_words = ['a', 'ab', 'bcd', 'c', 'd']
        result = ['ab', 'c', 'd']
        self.assertEqual(max_len_combination(sentence, list_words), sorted(result))

    def test_4(self):
        sentence = 'sixixi'
        list_words = ['s', 'si', 'sixi', 'ix', 'xi']
        result = ['si', 'xi', 'xi']
        self.assertEqual(max_len_combination(sentence, list_words), sorted(result))


### INUIT ###
#     parent_child_pairs = [
#         [1, 3],
#         [2, 3],
#         [3, 6],
#         [5, 6],
#         [5, 7],
#         [4, 5],
#         [4, 8],
#         [8, 10]
#     ]

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


### AFFIRM ###

# name_list = ["cheapair", "cheapoair", "peloton", "pelican"]
def shortestUniqueSubstr(name_list):
    result = {}

    for name in name_list:
        result[name] = name

        for i in range(len(name)):
            for j in range(i + 1, len(name)):
                substring = name[i: j]
                add_substring = True
                for name2 in name_list:
                    if (name2 != name) and (substring in name2):
                        add_substring = False
                        break

                if add_substring and len(substring) < len(result[name]):
                    result[name] = substring

    return result


def shortestUniqueSubstr2(name_list):
    def get_substrings(word):
        substrings = set()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                substrings.add(word[i:j])

        return substrings

    substrings = {word: get_substrings(word) for word in name_list}
    result = {}
    for key, value in substrings.items():
        value_temp = set(value)
        for key2, value2 in substrings.items():
            if key != key2:
                value_temp -= value2
        result[key] = min(value_temp, key=len)

    return result


### Stripe ###
client = "fr-FR, fr"
server = ["en-US", "fr-FR", "fr-CA"]


def combine(mylist):
    mydict = {}
    for lan in mylist:
        key = lan
        mydict[lan] = [lan]
        if len(lan) == 5:
            key = lan[:2]
        mydict[key] = mydict.get(key, list()) + [lan]

    return mydict


def is_accepted_simple(client, server):
    myclient = [lan.strip() for lan in client.split(",")]
    return set(myclient).intersection(set(server))


def is_accepted(client, server):
    accepted_langs = []
    dict_server = combine(server)
    for client_lan in client.split(","):
        cleaned_client_lan = client_lan.strip()
        server_langs = dict_server.get(cleaned_client_lan, None)
        if server_langs:
            accepted_langs += list(set(server_langs) - set(accepted_langs))

    return accepted_langs


if __name__ == '__main__':
    pass