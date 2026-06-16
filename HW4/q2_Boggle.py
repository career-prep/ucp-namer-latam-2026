"""
problem:
    - given a list of word (array)
    - given a board of char (2D array)
    - return a list of found word 

idea:
    we create trie for every word
    after created a trie, we do dfs to explore every char in board and keep checking with the trie




"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.validWord = False
    
    def addWord(self, word):
        curr = self

        for char in word:
            idx = ord(char) - ord("a")

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
        
            curr = curr.children[idx]
    
        curr.validWord = True

        return 

def boggle(words, board): 
    ###############################
    #Build Trie contain every node           
    ###############################
    root = TrieNode()

    for word in words:
        root.addWord(word.lower())
    

    # set up for dfs
    rows = len(board)
    cols = len(board[0])

    # use when do dfs in the board
    res = set()
    visited = set()

    # 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    #################
    # DFS
    #################  
     
    # node is the current char in Trie 
    # path: word formed so far
    # dfs is used to explore the board
    def dfs(r,c, node, path):
        # base case: out of bound or already use the cell -> stop exploring 
        # (we can not reuse same cell in 1 word)
        if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited:
            return 
        
        current_char = board[r][c].lower()
        idx = ord(current_char) - ord("a")

        # base case: when the prefix does not exist in trie
        if node.children[idx] is None:
            return 
        
        #board and trie move 1 step
        visited.add((r,c))
        node = node.children[idx]
        
        path += current_char

        if node.validWord:
            res.add(path)
        
        for dr, dc in directions:
            dfs(r+dr, c+dc, node, path)
        
        #backtrack
        visited.remove((r,c))
    

    for r in range(rows):
        for c in range(cols):
            dfs(r,c, root, "")
    
    return list(res)



        




