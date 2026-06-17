# This is as far as I got for my implementation in 40 minutes.
# Not storing the nodes "data" directly inside of it like we usually
# do felt very tricky at first

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self,char):
        return ord(char) - ord('a')

    def indexToChar(self,idx):
        return chr(ord('a') + idx)
    
    def insert(self, word):
        curr = self.root
        for c in word:
            c_idx = self.charToIndex(c)
            if curr.children[c_idx] is None:
                curr.children[c_idx] = TrieNode()
            curr = curr.children[c_idx]

        curr.validWord = True   

    def isValidWord(self, word):
        curr = self.root
        for c in word:
            c_idx = self.charToIndex(c)
            if curr.children[c_idx] is None:
                return False
            else:
                curr = curr.children[c_idx]

        return curr.validWord

    def remove(self, word):
         
         def dfs_helper(node, word, depth):
            if depth == len(word):
                if not node.validWord:
                    return False
            
            node.validWord = False

            

