# Question 1: Build a Trie

# Implements a Trie with insert, isValidWord, and remove methods.
# Each TrieNode has 26 children (one per lowercase letter) and a
# validWord flag marking end-of-word.

# Time Complexity:
#   insert:      O(m) where m = word length
#   isValidWord: O(m)
#   remove:      O(m)
# Space Complexity: O(TOTAL_CHARS) across all inserted words


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.validWord = True
    # Time Complexity = O(m), Space Complexity = O(m)

    def isValidWord(self, word):
        node = self.root
        for ch in word.lower():
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.validWord
    # Time Complexity = O(m), Space Complexity = O(1)

    def remove(self, word):
        self._remove(self.root, word.lower(), 0)
    # Time Complexity = O(m), Space Complexity = O(m) call stack

    def _remove(self, node, word, depth):
        if node is None:
            return None
        if depth == len(word):
            node.validWord = False
            if not any(node.children):
                return None
            return node
        idx = ord(word[depth]) - ord('a')
        node.children[idx] = self._remove(node.children[idx], word, depth + 1)
        if not node.validWord and not any(node.children):
            return None
        return node


# --- Tests ---

trie = Trie()
words = ["apple", "app", "apt", "bat", "ball"]
for w in words:
    trie.insert(w)

print("isValidWord('apple'):", trie.isValidWord("apple"))   # True
print("isValidWord('app'):", trie.isValidWord("app"))       # True
print("isValidWord('ap'):", trie.isValidWord("ap"))         # False
print("isValidWord('bat'):", trie.isValidWord("bat"))       # True
print("isValidWord('ba'):", trie.isValidWord("ba"))         # False

trie.remove("app")
print("After remove('app'):")
print("isValidWord('app'):", trie.isValidWord("app"))       # False
print("isValidWord('apple'):", trie.isValidWord("apple"))   # True (prefix shared, not deleted)

trie.remove("apple")
print("After remove('apple'):")
print("isValidWord('apple'):", trie.isValidWord("apple"))   # False
print("isValidWord('apt'):", trie.isValidWord("apt"))       # True (unrelated word preserved)

trie.remove("nonexistent")  # should not crash
print("isValidWord('bat'):", trie.isValidWord("bat"))       # True

# Spent a total of 35 mins on this question
