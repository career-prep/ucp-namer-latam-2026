# technique: Trie as a parameter
# time complexity: O(W*m + R*C*4^(R*C)) where W=dict size, m=avg word len, R/C=board dims
# space complexity: O(W*m) for trie + O(R*C) for visited
# time taken: 40 mins

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

def boggle(board, dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node, visited):
        ch = board[r][c].lower()
        if ch not in node.children:
            return
        next_node = node.children[ch]
        if next_node.word:
            found.add(next_node.word)
        visited.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, next_node, visited)
        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, set())

    return sorted(found)


dictionary = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay",
    "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape",
    "Trace", "Trap", "Tray", "Yap"
]

board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"]
]

print(boggle(board, dictionary))
