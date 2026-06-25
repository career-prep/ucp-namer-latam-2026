

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

    def delete(self, word):
        head = self.root
        for c in word:
            if c not in head.children:
                return False
            head = head.children[c]

        if not head.end:
            return False
        return self.helper(word)

    def helper(self, word):
        help = self.root
        for c in word:
            if len(help.children[c]) == 0 and head.end == False:
                del help.children[c]
            help = help.children[c]
