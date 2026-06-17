# Question 2: Boggle
# Given a Boggle board and a dictionary of valid words, return all valid words
# on the board. Valid words must be at least three characters and formed from
# non-overlapping adjacent letters, including diagonals.

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None

def build_trie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        lowered = word.lower()
        for char in lowered:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    return root

def boggle(board, dictionary):
    if not board or not board[0]:
        return []
    root = build_trie([word for word in dictionary if len(word) >= 3])
    rows = len(board)
    cols = len(board[0])
    found = set()
    visited = set()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    def dfs(row, col, node):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if (row, col) in visited:
            return
        char = board[row][col].lower()
        if char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            found.add(next_node.word)
        visited.add((row, col))
        for row_delta, col_delta in directions:
            dfs(row + row_delta, col + col_delta, next_node)
        visited.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, root)
    return sorted(found)

dictionary = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace",
    "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race",
    "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap",
]
board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"],
]
print(boggle(board, dictionary))
print(boggle([["A", "B"], ["C", "D"]], ["ab", "abc", "abd", "abcd"]))
print(boggle([], dictionary))




# Spent 40 mins
# Time Complexity: O(m * n * L), where L is the max word length.
# Space Complexity: O(W * L + m * n), for the trie and DFS visited path.
