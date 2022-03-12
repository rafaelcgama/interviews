import unittest


### GOOGLE ###

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

    def test_4(self): # Problem
        sentence = 'sixixi'
        list_words = ['s', 'si', 'sixi', 'ix', 'xi']
        result = ['si', 'xi', 'xi']
        self.assertEqual(max_len_combination(sentence, list_words), sorted(result))


if __name__ == '__main__':
    sentence = 'sixixi'
    list_words = ['s', 'si', 'sixi', 'ix', 'xi']

    remove_word(sentence, list_words)
