

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        cur = self.head
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.end = True

    """def print_trie(self, node=None, depth=0):
        if node is None:
            node = self.head
        for ch, child in node.children.items():
            marker = " *" if child.end else ""
            print("  " * depth + ch + marker)
            self.print_trie(child, depth + 1)
            """

board = [
    ['a', 'd', 'e'],
    ['r', 'c', 'p'],
    ['l', 'a', 'y']
]

dictionary = [
    "ace", "ape", "cape", "clap", "clay",
    "gape", "grape", "lace", "lap", "lay",
    "mace", "map", "may", "pace", "pay",
    "race", "rap", "ray",
    "tap", "tape", "trace",
    "trap", "tray", "yap"
]

tree = Trie()
for each in dictionary:
    tree.insert(each)
tree.print_trie()
