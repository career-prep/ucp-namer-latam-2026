# Question 2: Boggle

# Technique: Trie as a parameter
# Build a trie from the dictionary. Then DFS from each cell on the board,
# walking the trie simultaneously to prune branches that can't form valid
# words. This avoids checking every possible path against the dictionary.

# Time Complexity:  O(N*M * 8^L) where N*M is board size and L is max word
#                   length; trie pruning makes practical performance much
#                   better than the worst case.
# Space Complexity: O(W*L) for the trie (W words, L avg length) + O(L) stack


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None  # stores full word if this node ends a valid word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word


def boggle(board, rows, cols, dictionary):
    trie = Trie()
    for word in dictionary:
        if len(word) >= 3:
            trie.insert(word)

    found = set()

    def dfs(r, c, node, visited):
        ch = board[r][c].lower()
        idx = ord(ch) - ord('a')
        next_node = node.children[idx]
        if next_node is None:
            return
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

    # Return words in dictionary order to match expected output.
    # found contains original-case words as stored by trie.insert.
    result = []
    for word in dictionary:
        if word in found:
            result.append(word)
    return result


# --- Tests ---

dictionary = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape",
    "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace",
    "Pay", "Race", "Rap", "Ray", "Tap", "Tape", "Trace",
    "Trap", "Tray", "Yap"
]

# Board (3x3):
# A D E
# C P L
# Y A R  <- wait, the board given is A,D,E,R,C,P,L,A,Y read as:
# A D E
# R C P  <- actually looking at task: A D E / R C P / L A Y? Let me re-check.
# L A Y
# The task shows: A,D,E,R,C,P,L,A,Y which is a 3x3:
# A D E
# R C P
# L A Y

board = [
    ['A', 'D', 'E'],
    ['R', 'C', 'P'],
    ['L', 'A', 'Y'],
]

result = boggle(board, 3, 3, dictionary)
print("Boggle results:", result)
# Expected: Ace, Race, Pace, Lace, Pay, Lay, Clay, Ray, Lap, Rap, Clap, Ape, Cape, Yap

# Additional test: empty board
print("Empty dict:", boggle(board, 3, 3, []))

# Spent a total of 40 mins on this question
