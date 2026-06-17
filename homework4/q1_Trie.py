"""
Trie Methods

n is the length of the word

insert(word)
    Time: O(n)
    Space: O(1)

isValidWord(word)
    Time: O(n)
    Space: O(1)

remove(word)
    Time: O(n)
    Space: O(n) for call stack
"""
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.validWord = True


    def insert(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is not None:
                curr = curr.children[i]
            else:
                node = TrieNode()
                curr.children[i] = node
                curr = node
        curr.validWord = True

    def isValidWord(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            else:
                curr = curr.children[i]
        return True if curr.validWord else False

    # Assume that you can't remove empty string
    def remove(self, word):
        def deleteTrieNode(curr, idx, word):
            if not curr:
                return None
            if idx == len(word)-1:
                curr.validWord = False
            elif idx < len(word)-1:
                i = ord(word[idx+1]) - ord("a")
                curr.children[i] = deleteTrieNode(curr.children[i], idx+1, word)

            isEmpty = True
            for child in curr.children:
                if child:
                    isEmpty = False

            if isEmpty and not curr.validWord:
                return None
            else:
                return curr
        if not self.isValidWord(word) or word == "":
            return
        i = ord(word[0]) - ord("a")
        self.root.children[i] = deleteTrieNode(self.root.children[i], 0, word)

    def printTrie(self):
        def dfs(node, prefix):
            if node.validWord:
                print(prefix)

            for i, child in enumerate(node.children):
                if child:
                    dfs(child, prefix + chr(i + ord("a")))

        dfs(self.root, "")

trie = Trie()

words = ["dog", "do", "dad", "doge"]
for word in words:
    trie.insert(word)
trie.printTrie()

print(trie.isValidWord("bad") == False)
print(trie.isValidWord("dad") == True)
print(trie.isValidWord("") == True)
print(trie.isValidWord("dads") == False)

trie.remove("doge")
trie.printTrie()
trie.remove("")
trie.printTrie()
trie.remove("bad")
trie.printTrie()

# Time Spent: 50:00
