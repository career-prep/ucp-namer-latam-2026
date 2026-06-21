# technique: Trie data structure implementation
# time complexity: insert O(m), search O(m), delete O(m) where m = word length
# space complexity: O(n * m) where n = number of words, m = average word length
# time taken: 38 mins

class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.valid_word = True

    def isValidWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.valid_word

    def remove(self, word):
        def _remove(node, word, depth):
            if depth == len(word):
                if not node.valid_word:
                    return False
                node.valid_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _remove(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.valid_word
            return False

        _remove(self.root, word, 0)


trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apt")
trie.insert("bat")

print(trie.isValidWord("apple"))   # True
print(trie.isValidWord("app"))     # True
print(trie.isValidWord("ap"))      # False
print(trie.isValidWord("bat"))     # True
print(trie.isValidWord("cat"))     # False

trie.remove("app")
print(trie.isValidWord("app"))     # False
print(trie.isValidWord("apple"))   # True (apple still exists)

trie.remove("apple")
print(trie.isValidWord("apple"))   # False
print(trie.isValidWord("apt"))     # True (apt still exists)
