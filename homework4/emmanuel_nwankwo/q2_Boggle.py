# Technique: Trie as a parameter
# Time Complexity: O(W * L + rows * cols * 8^L)
# Space Complexity: O(W * L + rows * cols)

from q1_BuildATrie import Trie

def Boggle(board, dictionary):
    trie = Trie()

    for word in dictionary:
        trie.insert(word.lower())

    rows = len(board)
    cols = len(board[0])
    results = set()
    visited = set()

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def dfs(r, c, node, word):
        if node.validWord and len(word) >= 3:
            results.add(word)

        visited.add((r, c))

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                ch = board[nr][nc].lower()
                index = ord(ch) - ord('a')

                if node.children[index] is not None:
                    dfs(nr, nc, node.children[index], word + ch)

        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            ch = board[r][c].lower()
            index = ord(ch) - ord('a')

            if trie.root.children[index] is not None:
                dfs(r, c, trie.root.children[index], ch)

    return list(results)

# Time Taken: 20mins 14secs

#Testcases:
board_1 = [
    ['A', 'D', 'E'],
    ['R', 'C', 'P'],
    ['L', 'A', 'Y']
]
dictionary_1 = [
    "Ace", "Ape", "Cape", "Clap", "Clay",
    "Gape", "Grape", "Lace", "Lap", "Lay",
    "Mace", "Map", "May", "Pace", "Pay",
    "Race", "Rap", "Ray", "Tap", "Tape",
    "Trace", "Trap", "Tray", "Yap"
]
print(Boggle(board_1, dictionary_1))

# Edge cases:
board_2 = [
    ['A', 'B'],
    ['C', 'D']
]
dictionary_2 = [] # Empty dictionary
print(Boggle(board_2, dictionary_2))

board_3 = [ # Single cell board
    ['A']
]
dictionary_3 = [
    "A",
    "AA",
    "AAA"
]
print(Boggle(board_3, dictionary_3))