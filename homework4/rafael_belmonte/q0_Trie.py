class TrieNode:
    def __init__(self):
        self.children = {}
        self.isleaf = False

    def insert(self, word): #O(n) where n is the length of the word
        current = self
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.isleaf = True

    def isValidWord(self, word): #O(n) where n is the length of the word
        current = self
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.isleaf

    def remove(self, word): #
        def helper(node, word, index):
            if index == len(word):
                if not node.isleaf:
                    return False
                node.isleaf = False
                return len(node.children) == 0
            character = word[index]
            if character not in node.children:
                return False
            if helper(node.children[character], word, index + 1):
                del node.children[character]
                return len(node.children) == 0 and not node.isleaf
            return False
        helper(self, word, 0)

#test cases

trie = TrieNode()
trie.insert("hello")
assert(trie.isValidWord("hello") == True)
assert(trie.isValidWord("hell") == False)
trie.remove("hello")
assert(trie.isValidWord("hello") == False)
assert(trie.isValidWord("hell") == False)
assert(trie.isValidWord("hi") == False)
trie.insert("hi")
assert(trie.isValidWord("hi") == True)
trie.remove("helaffw")
assert(trie.isValidWord("hi") == True)

# edge cases
trie.insert("hell")
trie.insert("hello")
assert(trie.isValidWord("hell") == True)
assert(trie.isValidWord("hello") == True)
trie.remove("hell")
assert(trie.isValidWord("hell") == False)
assert(trie.isValidWord("hello") == True)
trie.remove("hello")
assert(trie.isValidWord("hello") == False)
assert(trie.isValidWord("hi") == True)

trie.insert("same")
trie.insert("same")
assert(trie.isValidWord("same") == True)
trie.remove("same")
assert(trie.isValidWord("same") == False)

print("yay!!")

# Time spent: ~30 minutes
