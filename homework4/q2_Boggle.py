# Array/String Technique: 1. Trie as a parameter
# Time Complexity: O(M * L + R * C * 8^L) where M is number of words, L is max word length, and R, C are board dimensions
# Space Complexity: O(M * L) 

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    root = {}
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = word

    rows, cols = len(board), len(board[0])
    matched_words = []

    def dfs(r, c, parent):
        char = board[r][c]
        curr_node = parent[char]

        word_match = curr_node.pop('$', None)
        if word_match:
            matched_words.append(word_match)

        board[r][c] = '#'
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                dfs(nr, nc, curr_node)
        board[r][c] = char

        if not curr_node:
            parent.pop(char)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root:
                dfs(r, c, root)

    return matched_words

if __name__ == "__main__":
    board = [
        ['A', 'D', 'E'],
        ['R', 'C', 'P'],
        ['L', 'A', 'Y']
    ]
    words = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]
    # Adjust dictionary matching lowercase/uppercase inputs appropriately
    lowercase_board = [[c.lower() for c in row] for row in board]
    lowercase_words = [w.lower() for w in words]
    results = findWords(lowercase_board, lowercase_words)
    print("Found words:", [w for w in words if w.lower() in results])

# Time Spent: 35 minutes