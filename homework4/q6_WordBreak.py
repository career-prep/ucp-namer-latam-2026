# Runtime: O(2^n) better solution definitely exists.
# Space complexity: O(n + d*m) where d is the number of words in a dictionary and m is the avg len of the words. n or d*m could dominate.
# Technique: Trie as a parameter
class TrieNode():
    def __init__(self):
        self.chars = [None] * 26
        self.validWord = False
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            nxt = ord(c) - ord('a')
            if curr.chars[nxt]:
                curr = curr.chars[nxt]
            else:
                newNode = TrieNode()
                curr.chars[nxt] = newNode
                curr = newNode
        curr.validWord = True

    def isPrefix(self, word):
        curr = self.root
        for c in word:
            nxt = ord(c)-ord('a')
            if not curr.chars[nxt]:
                return False
            else:
                curr = curr.chars[nxt]
        return True

    def isWord(self, word):
        curr = self.root
        for c in word:
            nxt = ord(c)-ord('a')
            if not curr.chars[nxt]:
                return False
            else:
                curr = curr.chars[nxt]
        return True if curr.validWord else False


def wordBreak(dictionary, s):
    if not s: # Assuming that an empty string cannot be broken up into two words that are both empty strings
        return False
    trie = Trie()
    for word in dictionary:
        trie.insert(word)


    def helper(trie, s, i,):
        if i > len(s)-1:
            return True
        if not trie.isPrefix(s[0:i+1]):
            return False

        if trie.isWord(s[0:i+1]):
            return helper(trie, s[i+1:], 0) or helper(trie, s, i+1)

        return helper(trie, s, i+1)

    return helper(trie, s, 0)

dictionary = ["elf", "go", "golf", "man", "manatee", "not", "note", "pig", "quip", "tee", "teen"]
print(wordBreak(dictionary, "mangolf"))
print(wordBreak(dictionary, "manateenotelf"))
print(wordBreak(dictionary, "quipig"))
print(wordBreak(dictionary, ""))
print(wordBreak(dictionary, "man")) # Assuming True is correct because adding spaces means that you don't necessarily have to add one to make valid words.

# Time Spent: 40:00
