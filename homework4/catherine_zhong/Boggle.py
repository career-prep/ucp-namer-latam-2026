#trie and dfs
#time complexity: O(n^2)
#space complexity: O(N)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def index(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        node = self.root

        for char in word:
            idx = self.index(char)

            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            node = node.children[idx]
        node.validWord = True
        return

    def isValidWord(self, word):
        node = self.root
        
        for char in word:
            idx = self.index(char)

            if node.children[idx] is None:
                return False
            
            node = node.children[idx]

        return node is not None and node.validWord

    def remove(self, word):
        
        def helper(node, depth):
            if node is None:
                return False

            if depth == len(word):
                if not node.validWord:
                    return False
                node.validWord = False

            else:
                idx = self.index(word[depth])
                child = node.children[idx]
                if helper(child, depth+1):
                    node.children[idx] = None

            if node is not self.root:
                c = any(child is not None for child in node.children)
                if not c and not node.validWord:
                    return True
            return False

        helper(self.root, 0)


def Boggle(dictionary, board):
    if not board:
        return []

    validWords = Trie()

    for i in dictionary:
        validWords.insert(i)
    
    result = set()

    rows, cols = len(board), len(board[0])
    currLetters = []
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, -1), (-1, 0), (-1, 1),( 0, -1),( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]

    def dfs(row, col, node):
        if row < 0 or row >= len(board):
            return
        if col < 0 or col >= len(board[0]):
            return

        if visited[row][col]:
            return

        char = board[row][col]
        i = validWords.index(char)

        if node.children[i] is None:
            return

        nextNode = node.children[i]
        visited[row][col] = True
        currLetters.append(char)
        if nextNode.validWord and len(currLetters) >=3:
            result.add(''.join(currLetters))

        for r,c in directions:
            dfs(row + r, col + c, nextNode)
        
        currLetters.pop()
        visited[row][col] = False

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, validWords.root)

    return list(result)


#test cases
board = [
    ['c', 'a', 't'],
    ['a', 'n', 'o'],
    ['p', 'r', 's']
]
dictionary = ["cat", "can", "car", "dog"]
print(Boggle(dictionary, board))

# 2. No valid words at all
board2 = [
    ['x', 'y'],
    ['z', 'q']
]
dictionary2 = ["cat", "dog"]
print(Boggle(dictionary2, board2))