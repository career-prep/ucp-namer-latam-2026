class Node():
    def __init__(self):
        self.children = {}
        self.validWord = False

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.validWord = True

    def isValidWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.validWord

    def remove(self, word):
        self._remove(self.root, word, 0)

    def _remove(self, cur, word, index):
        if index == len(word):
            if not cur.validWord:
                return False 
            cur.validWord = False

            return len(cur.children) == 0
        
        c = word[index]
        node = cur.children.get(c)

        if node is None:
            return False
        delete_current_node = self._remove(node, word, index + 1)
        if delete_current_node:
            del cur.children[c]
            return len(cur.children) == 0 and not cur.validWord
        return False
    

trie = Trie()
trie.insert("apple")
print(trie.isValidWord('apple')) # T
print(trie.isValidWord('app')) # F
print(trie.isValidWord('banana')) # F


trie.insert("app")
print(trie.isValidWord('app')) # T

trie.remove("orange") 
print(trie.isValidWord('apple')) # T


trie.insert("banana")
print(trie.isValidWord('banana')) # T
trie.remove("banana")
print(trie.isValidWord('banana')) # F


trie.remove("app")
print(trie.isValidWord('app')) # F
print(trie.isValidWord('apple')) # T


trie.insert("app") 
trie.remove("apple")
print(trie.isValidWord('apple')) # F
print(trie.isValidWord('app')) # T

# 40 Mins