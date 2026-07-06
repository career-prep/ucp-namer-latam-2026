# Method: Trie + DFS
# Space Complexity: O(N)
# Time Complexity: O(NLogN) Not really sure about space and time complexity.
# Total Time Taken: 40 mins
# Turn the dictionary into a trie so that you can easily retrieve whether a word is valid. 
# Use DFS to search through different paths on the board and check with the trie on whether a word is in the dictionary. If it is, add it to the results list.

class Node():
    def __init__(self):
        self.children = {}
        self.validWord = False

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.validWord = True

    def isValidWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.validWord
    
    def getChild(self, cur, char):
        if cur and char in cur.children:
            return cur.children[char]
        return None
    
def Boggle(board, dictionary):
    trie = Trie()

    for word in dictionary:
        trie.insert(word)

    row = len(board)
    col = len(board[0])
    visited = set()
    found = set()

    def dfs(r, c, curNode, curWord):
        if (r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited):
            return
        char = board[r][c]
        nextNode = trie.getChild(curNode, char)
        if not nextNode:
            return 
        
        curWord += char
        if nextNode.validWord:
            found.add(curWord)

        visited.add((r, c))
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            dfs(r + dr, c + dc, nextNode, curWord)

        visited.remove((r, c))

    for r in range(row):
        for c in range(col):
            dfs(r, c, trie.root, "")
    return list(found)
    
board = [
    ['A', 'D', 'E'],
    ['R', 'C', 'P'],
    ['L', 'A', 'Y']
]

dictionary = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay",
    "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape", 
    "Trace", "Trap", "Tray", "Yap"
]

print(Boggle(board, [word.upper() for word in dictionary]))