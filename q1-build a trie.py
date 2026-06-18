class TriNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


def insert(self, word):
    curr = self
    for ch in word:
        index = ord(ch) - ord('a')
        if curr.children[index] is None:
            curr.children[index].TriNode()
        curr = curr.children[index]
    curr.isEndOfWord = True

def isValidWord(self, word):
    curr = self
    for ch in word:
        index = ord(ch) - ord('a')
        if curr.children[index] is None:
            return False
        curr = curr.children[index]
    return curr.isEndOfWord 

def remove(word):

    def helper(node, word, depth = 0):
        if depth == len(word):
            node.isEndOfWord = False
            return all(child is None for child in node.children)
        
        ch = word[depth]
        index = ord(ch) - ord('a')
        can_delete = helper(node.children[index], word, depth + 1)

        if can_delete:
            node.children[index] = None 
        return not node.isEndOfWord and all(child is None for child in node.children)
    
    return helper(self,word, 0)