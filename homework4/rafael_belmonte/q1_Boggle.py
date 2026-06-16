# Technique: Trie as a parameter
# time complexity: O(m * n * 8^L) where L is the longest word, with trie pruning
# space complexity: O(W * L) for the trie and O(L) for the recursive path

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isleaf = False


def boggle(board, dictionary):
    if not board or not board[0]:
        return []

    root = TrieNode()
    for word in dictionary:
        if len(word) >= 3:
            curr = root
            for char in word.lower():
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isleaf = True

    rows = len(board)
    cols = len(board[0])
    result = set()
    visited = set()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    def dfs(row, col, node, word):
        char = board[row][col].lower()
        if char not in node.children:
            return

        node = node.children[char]
        word += char
        if node.isleaf:
            result.add(word)

        visited.add((row, col))
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols and
                    (new_row, new_col) not in visited):
                dfs(new_row, new_col, node, word)
        visited.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, root, "")

    return list(result)



#test cases
dictionary = ["Ace", "Ape", "Cape", "Clap", "Clay",
              "Gape", "Grape", "Lace", "Lap", "Lay",
              "Mace", "Map", "May", "Pace", "Pay",
              "Race", "Rap", "Ray", "Tap", "Tape", "Trace",
              "Trap", "Tray", "Yap"]
board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"],
]

assert sorted(boggle(board, dictionary)) == sorted([
    "ace", "race", "pace", "lace", "pay", "lay", "clay", "ray", "lap",
    "rap", "clap", "ape", "cape", "yap"
])

# edge cases
assert boggle([], dictionary) == []
assert boggle(board, []) == []
assert boggle([["A"]], ["a", "at", "ate"]) == []

small_board = [
    ["C", "A"],
    ["T", "S"],
]
assert sorted(boggle(small_board, ["cat", "cats", "cast", "act",
                                   "acts", "sat", "tac"])) == sorted([
    "cat", "cats", "cast", "act", "acts", "sat", "tac"
])
assert boggle(small_board, ["cat", "cat"]).count("cat") == 1

reuse_board = [
    ["A", "B"],
    ["C", "D"],
]
assert sorted(boggle(reuse_board, ["aba", "aaaa", "abc"])) == ["abc"]

print("yay!!")

# Time spent: ~35 minutes
