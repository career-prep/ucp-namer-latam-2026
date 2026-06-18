class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self
        for ch in word:
            index = ord(ch) - ord('a')
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEndOfWord = True

    def isValidWord(self, word):
        curr = self
        for ch in word:
            index = ord(ch) - ord('a')
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEndOfWord 

    def remove(word):

        def helper(node, word, depth = 0):
            if depth == len(word):
                node.isEndOfWord = False
                return all(child is None for child in node.children)
            
            ch = word[depth]
            index = ord(ch) - ord('a')
            can_delete = helper(node.children[index], word, depth + 1)

            if can_delete:
                node.children[index] = None 
            return not node.isEndOfWord and all(child is None for child in node.children)
        
        return helper(self,word, 0)

def Boggle(Dictionary, board):
    trie = Trie()
    for word in Dictionary:
        trie.insert(word)
    
    visited = set()
    res = []
    def dfs(r, c, trie_node, path):

        if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visited):
            return

        ch = board[r][c]
        if ch not in trie_node.children:
            return
        trie_node = trie_node.children[ch]

        if trie_node.isEndOfWord:
            res.append(path+ch)

        visited.add((r,c))
        dfs(r+1,c,trie_node,path + ch)
        dfs(r+1,c+1,trie_node,path + ch)
        dfs(r-1,c,trie_node,path + ch)
        dfs(r+1,c-1,trie_node,path + ch)
        dfs(r,c+1,trie_node,path + ch)
        dfs(r-1,c+1,trie_node,path + ch)
        dfs(r,c-1,trie_node,path + ch)
        dfs(r-1,c-1,trie_node,path + ch)
        visited.remove((r,c))
        return 
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(r,c,trie.root,"")
    return res