class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # Resizable or fixed array of size 26
        self.validWord = False # Bool flag to indicate if the node marks the end of a valid word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Adds a word to the trie
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        
        curr.validWord = True

    # Returns a boolean indicating whether word is in the trie
    def isValidWord(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        
        return curr.validWord
    
    # Removes word from the trie & deletes unused nodes
    def remove(self, word: str) -> None:
        curr = self.root
        path = [curr]

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return
            curr = curr.children[index]
            path.append(curr)
        
        if not curr.validWord:
            return

        curr.validWord = False

        for i in range(len(word) -1, -1, -1):
            parent = path[i]
            child = path[i + 1]
            index = ord(word[i]) - ord('a')
            if any(c is not None for c in child.children) or child.validWord:
                break

            parent.children[index] = None

# Time Spent: 27 minutes