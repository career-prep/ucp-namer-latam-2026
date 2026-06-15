# Runtime: O(V^2*8^L*L), V is # of vertices and L is max word length. ???
# Space complexity: O(D*M), D is # of dictionary words and M is the avg length of the words
# Technique: Trie as a parameter
def boggle(board, dictionary):
    if not board:
        return []
    if not dictionary:
        return []
    # Note to self: Next time define the class outside the method
    class TrieNode():
        def __init__(self):
            self.children = [None] * 26
            self.validWord = False
    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            curr = self.root
            for c in word:
                i = ord(c) - ord("A")
                if not curr.children[i]:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
            curr.validWord = True

        def isPrefix(self, key):
            curr = self.root
            for c in key:
                i = ord(c) - ord('A')
                if curr.children[i]:
                    curr = curr.children[i]
                else:
                    return False
            return True

        def isValidWord(self, word):
            curr = self.root
            for c in word:
                i = ord(c) - ord('A')
                if curr.children[i]:
                    curr = curr.children[i]
                else:
                    return False
            return True if curr.validWord else False

    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    # instead of passing a string I should have passed a trieNode that way I don't have to start from the beginning each time to check if the prefix exists. Improves runtime.
    def dfs(source, board, trie, visited, curr, res):
        if trie.isValidWord(curr) and len(curr) >= 3:
            res.add(curr)
        dirs = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
        rows = len(board)
        cols = len(board[0])
        r,c = source
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                ncurr = curr + board[nr][nc]
                if trie.isPrefix(ncurr):
                    visited.add((nr,nc))
                    dfs((nr,nc), board, trie, visited, ncurr, res)
                    visited.remove((nr,nc))
        return res

    rows = len(board)
    cols = len(board[0])
    res = set()
    for i in range(rows):
        for j in range(cols):
            visited = set()
            visited.add((i,j))
            dfs((i,j), board, trie, visited, board[i][j], res)

    return list(res)

board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"]
]
dictionary = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]
dictionary = [word.upper() for word in dictionary]
expected = ["Ace", "Race", "Pace", "Lace", "Pay", "Lay", "Clay", "Ray", "Lap", "Rap", "Clap", "Ape", "Cape", "Yap"]
expected = [word.upper() for word in expected]

print(sorted(boggle(board, dictionary)) == sorted(expected)) # general case
print(boggle(None, dictionary) == []) # null test
print(boggle(board, None) == []) # null test
print(boggle(board, ["XAD",]) == []) # Testing word that DNE
print(sorted(boggle(board, dictionary + ["A"])) == sorted(expected)) # Testing min length of 3


# Time Spent: 50:00
