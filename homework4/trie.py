# Part 1: Data Structure Implementation - Trie
# Time: O(L) per operation (L = word length)
# Space: O(total characters inserted)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.validWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.validWord = True

    def isValidWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.validWord

    def remove(self, word):
        self._removeHelper(self.root, word, 0)

    def _removeHelper(self, node, word, index):
        # returns True if this node is safe to delete
        if index == len(word):
            node.validWord = False
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        if self._removeHelper(node.children[char], word, index + 1):
            del node.children[char]
            return len(node.children) == 0 and not node.validWord
        return False


trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("card")
print(trie.isValidWord("car"))   # True
print(trie.isValidWord("ca"))    # False
trie.remove("car")
print(trie.isValidWord("car"))   # False
print(trie.isValidWord("card"))  # True

# Time spent: ~35 minutes