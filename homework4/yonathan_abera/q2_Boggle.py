# Technique: Trie as a parameter
# Time Complexity: O(N*8^L) search + O(dictionary chars)to build the trie
# Space Complexity: O(dictionary chars) + O(L)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def build_trie(dictionary):
    root = TrieNode()
    for w in dictionary:
        if len(w) < 3:
            continue
        node = root
        for ch in w.lower():
            node = node.children.setdefault(ch, TrieNode())
        node.word = w
    return root


def find_words(board, dictionary):
    if not board or not board[0]:
        return []
    root = build_trie(dictionary)
    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node, visited):
        ch = board[r][c].lower()
        if ch not in node.children:
            return
        node = node.children[ch]
        if node.word is not None:
            found.add(node.word)
        visited.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, node, visited)
        visited.discard((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, set())
    return sorted(found)

dictionary = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap",
    "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray",
    "Tap", "Tape", "Trace", "Trap", "Tray", "Yap",
]
board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"],
]
print(find_words(board, dictionary))
print(find_words([], dictionary))

# Time spent:50~
