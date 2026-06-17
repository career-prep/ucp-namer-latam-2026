class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        d = self.trie
 
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
 
        d['.'] = '.'

    def isValidWord(self, word):
        d = self.trie
 
        for c in word:
            if c not in d:
                return False
            d = d[c]
 
        return '.' in d

    def remove(self, word):
        d = self.trie
        stack = []

        for c in word:
            if c not in d:
                return False
            stack.append((d, c))
            d = d[c]

        if '.' not in d:
            return False

        del d['.']

        for parent, char in reversed(stack):
            child = parent[char]
            if child:
                break
            del parent[char]

        return True



#Time-taken: 30 minutes


import unittest


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_validate_word(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.isValidWord("hello"))

    def test_prefix_is_not_word(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.isValidWord("hell"))

    def test_remove_word(self):
        self.trie.insert("cat")
        self.trie.insert("car")

        self.assertTrue(self.trie.remove("cat"))
        self.assertFalse(self.trie.isValidWord("cat"))
        self.assertTrue(self.trie.isValidWord("car"))

    def test_remove_missing_word(self):
        self.trie.insert("dog")
        self.assertFalse(self.trie.remove("cat"))
        self.assertTrue(self.trie.isValidWord("dog"))


if __name__ == "__main__":
    unittest.main()