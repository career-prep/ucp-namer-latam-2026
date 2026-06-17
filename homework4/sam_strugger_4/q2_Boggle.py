# I'm not really sure what the time and space complexity of this solution is
# since there is so many moving parts

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self,char):
        return ord(char.lower()) - ord('a')

    def indexToChar(self,idx):
        return chr(ord('a') + idx)
    
    def insert(self, word):
        curr = self.root
        for c in word:
            c_idx = self.charToIndex(c)
            if curr.children[c_idx] is None:
                curr.children[c_idx] = TrieNode()
            curr = curr.children[c_idx]

        curr.validWord = True
        curr.word = word

def boggle(dictionary, board):
    """
    Approach:
    Put all of the words in a Trie
    Use DFS on the grid and see if we can match words on 
    the grid to dfs on the trie
    """
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    if not board or not board[0]:
        return []

    rows = len(board)
    columns = len(board[0])

    result = set()

    visited = set()

    def dfs(r, c, curr):
        if r < 0 or c < 0 or r >= rows or c >= columns:
            return

        if (r, c) in visited:
            return

        c_idx = trie.charToIndex(board[r][c])
        if curr.children[c_idx] is None:
            return

        next_node = curr.children[c_idx]

        if next_node.validWord:
            result.add(next_node.word)

        visited.add((r, c))

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, next_node)

        visited.remove((r, c))

    for r in range(rows):
        for c in range(columns):
            dfs(r, c, trie.root)

    return result


# Test Cases
dictionary1 = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]
board1 = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"]
]

test1 = boggle(dictionary1, board1)
print(test1)

# this took me 50 minutes
