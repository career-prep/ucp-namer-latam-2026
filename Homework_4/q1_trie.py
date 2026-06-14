# Question 1: Build a Trie
# Implement a trie class with insert, is_valid_word/search, and remove/delete.
# The trie should add words, report whether a word is present, and remove words
# while deleting unused nodes.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.valid_word = True
    def is_valid_word(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.valid_word
    def remove(self, word):
        word = word.lower()
        def delete(node, index):
            if index == len(word):
                if not node.valid_word:
                    return False
                node.valid_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            should_delete_child = delete(node.children[char], index + 1)
            if should_delete_child:
                del node.children[char]
            return not node.valid_word and len(node.children) == 0
        delete(self.root, 0)



        
trie = Trie()
for word in ["apple", "app", "ape", "bat"]:
    trie.insert(word)
print(trie.is_valid_word("apple"))
print(trie.is_valid_word("app"))
print(trie.is_valid_word("ap"))
print(trie.is_valid_word("bat"))
trie.remove("app")
print(trie.is_valid_word("app"))
print(trie.is_valid_word("apple"))
trie.remove("apple")
print(trie.is_valid_word("apple"))
print(trie.is_valid_word("ape"))



# Spent 35 mins
# Time Complexity:
# insert/search/remove are O(k), where k is the length of the word.
# Space Complexity:
# O(n * k), where n is the number of words and k is the average word length.
