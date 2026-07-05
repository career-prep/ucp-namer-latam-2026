


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        head = self.root
        for w in word:
            if w not in head.children:
                head.children[w] = TrieNode()
            head = head.children[w]
        head.end = True
    def remove(self, word):
        n = len(word)

        def dfs(idx, node):
            if idx == n:
                if node.end == False:
                    return node.end 
                node.end = False
                return len(node.children) == 0
            ch = word[idx]
            if ch not in node.children:
                return False
            delete =  dfs(idx +1, node.children[ch])
            if delete:
                del node.children[ch]
            return len(node.children) == 0 and node.end  == False
        
        dfs(0, self.root)

def boggle(dictionary, board):
    tree = Trie()
    for each in dictionary:
        tree.insert(each.upper())

    rows = len(board)
    cols = len(board[0])
    found = set()
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col, node, cur):
        letter = board[row][col].upper()
        if letter not in node.children:
            return 
        node = node.children[letter]
        visited[row][col] = True
        cur += letter
        if node.end == True:
            found.add(cur)

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if(0 <= new_row < rows and 0 <= new_col < cols and visited[new_row][new_col] == False):
                dfs(new_row, new_col, node, cur)
        visited[row][col] = False

    for r in range(rows):
        for c in range(cols):
            dfs(r,c,tree.root,"")
    return found

board = [
    ['a', 'd', 'e'],
    ['r', 'c', 'p'],
    ['l', 'a', 'y']
]

dictionary = [
    "ace", "ape", "cape", "clap", "clay",
    "gape", "grape", "lace", "lap", "lay",
    "mace", "map", "may", "pace", "pay",
    "race", "rap", "ray",
    "tap", "tape", "trace",
    "trap", "tray", "yap"
]

print(boggle(dictionary,board))

