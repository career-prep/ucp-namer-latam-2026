# Technique: Trie as a parameter

from q1_Build_A_Trie import Trie

def Boggle(board,dictionary):

    trie = Trie()

    for word in dictionary:
        trie.insert(word)
    
    rows = len(board)
    cols = len(board[0])
    result = set()
    visited = set()

    def dfs(row, col, curr, word):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        if (row, col) in visited:
            return

        char = board[row][col].lower()
        index = ord(char) - ord('a')

        if curr.children[index] is None:
            return

        curr = curr.children[index]
        word += char

        if curr.isEndOfWord:
            result.add(word)

        visited.add((row, col))

        directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
        ]

        for r_change, c_change in directions:
            dfs(row + r_change, col + c_change, curr, word)
        
        visited.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie.root, "")

    return list(result)


# dictionary = [
#     "Ace", "Ape", "Cape", "Clap", "Clay",
#     "Gape", "Grape", "Lace", "Lap", "Lay",
#     "Mace", "Map", "May", "Pace", "Pay",
#     "Race", "Rap", "Ray", "Tap", "Tape",
#     "Trace", "Trap", "Tray", "Yap"
# ]

# board = [
#     ["A", "D", "E"],
#     ["R", "C", "P"],
#     ["L", "A", "Y"]
# ]

# words = Boggle(board, dictionary)

# print(words)

# output = ['cape', 'ray', 'lay', 'ace', 'race', 'lap', 'ape', 'clap', 'pace', 'pay', 'lace', 'rap', 'yap', 'clay']