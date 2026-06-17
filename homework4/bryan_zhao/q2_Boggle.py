# Technique: Trie as a parameter
# Time Complexity: O (W X L) where W is the number of words in the dict and L is the max word length
# Space Complexity: O(W X L)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c.lower()) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        
        curr.word = word


def boggle(board: list[list[str]], dictionary: list[str]) -> list[str]:
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    found_words = set()

    def dfs(r, c, node):
        char = board[r][c]
        index = ord(char.lower()) - ord('a')

        if index < 0 or index >= 26 or not node.children[index]:
            return

        next_node = node.children[index]

        if next_node.word:
            found_words.add(next_node.word)

        board[r][c] = '#'

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
        
        board[r][c] = char

    for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
            
    return sorted(list(found_words))
    
dictionary_list = [
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay",
    "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape", 
    "Trace", "Trap", "Tray", "Yap"
]

boggle_board = [
    ['A', 'D', 'E'],
    ['R', 'C', 'P'],
    ['L', 'A', 'Y']
]

valid_words = boggle(boggle_board, dictionary_list)
print(valid_words)

# Time Spent: 40 minutes