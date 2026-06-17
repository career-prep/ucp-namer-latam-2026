from q1_Trie import Trie, TrieNode

# Time complexity: O(D * L), D = # of words in dictionary, L = average length of dictionary word
#                  O(N * 8^L) where N = board size (R * C)
#                  = O(D * L + N * 8^L)
# Space complexity: O(D * L) for trie storage

# Technique: Trie

DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def dfs(board, r, c, curr: TrieNode, currWord, result):
    # now we have visited this node
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == "-":
        return
    
    letter = board[r][c]
    idx = ord(letter) - ord('a')

    if curr.children[idx] is None:
        return

    curr = curr.children[idx]
    currWord.append(letter)

    if curr.validWord:
        result.add("".join(currWord))

    board[r][c] = "-"

    for dr, dc in DIRS:
        dfs(board, r + dr, c + dc, curr, currWord, result)

    # now backtrack
    board[r][c] = letter
    currWord.pop()


def Boggle(board, dictionary):
    # make the board lowercase
    board = [[ch.lower() for ch in row] for row in board]

    # build the Trie
    trie = Trie(TrieNode())
    curr = trie.root
    for word in dictionary:
        trie.insert(word)

    result = set()

    ROWS = len(board)
    COLS = len(board[0])

    for r in range(ROWS):
        for c in range(COLS):
            dfs(board, r, c, trie.root, [], result)

    return list(result)

if __name__ == "__main__":
    board = [["A", "D", "E"],
             ["R", "C", "P"],
             ["L", "A", "Y"]]
    
    dictionary = ["ace", "ape", "cape", "clap", "clay", "gape", "grape", "lace", "lap", "lay", "mace", "map", "may", "pace", "pay", "race", "rap", "ray", "tap", "tape", "trace", "trap", "tray", "yap"]

    valid_words = Boggle(board, dictionary)
    for word in valid_words:
        print(word)

# ~ time spent: ~35 minutes