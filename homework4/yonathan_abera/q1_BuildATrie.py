# Data Structure: Trie
# Time Complexity: O(L) per insert/search/remove
# Space Complexity: O(L) per inserted word

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.valid_word = False

    def has_children(self):
        return any(self.children)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.valid_word = True

    def isValidWord(self, word):
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                return False
            node = node.children[i]
        return node.valid_word

    def remove(self, word):
        self._remove(self.root, word, 0)

    def _remove(self, node, word, depth):
        if node is None:
            return False
        if depth == len(word):
            node.valid_word = False
            return not node.has_children()
        i = ord(word[depth]) - ord('a')
        if self._remove(node.children[i], word, depth + 1):
            node.children[i] = None
        return not node.valid_word and not node.has_children()

t = Trie()
for w in ["cat", "car", "card", "dog"]:
    t.insert(w)
print(t.isValidWord("cat"))
print(t.isValidWord("ca"))
print(t.isValidWord("cab"))
t.remove("car")
print(t.isValidWord("car"))
print(t.isValidWord("card"))
t.remove("zebra")
print(t.isValidWord("dog"))

# Time spent: 30
