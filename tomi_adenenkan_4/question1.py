

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        head = self.root

        for ch in data:
            if ch not in head.children:
                head.children[ch] = Node()
            head = head.children[ch]

        head.end = True

    def search(self, word):
        head = self.root
        for c in word:
            if c not in head.children:
                return False
            head = head.children[c]

        return head.end

    def deleting(self, word):
        n = len(word)

        def dfs(node, idx):
            if idx == n:
                if node.end == False:
                    return False
                node.end = False
                return len(node.children) == 0

            ch = word[idx]
            if ch not in node.children:
                return False
            delete = dfs(node.children, idx+1)
            if delete == True:
                del node.children[ch]

            return len(node.children) == 0 and node.end == False
                
                
