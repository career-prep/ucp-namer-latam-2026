from q1_build_a_trie import Trie, TrieNode

def boggle(board, dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word.lower())

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    found = set()

    DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    def dfs(r, c, node, path, visited):
        ch = board[r][c].lower()
        idx = ord(ch) - ord('a')

        if node.children[idx] is None:
            return

        next_node = node.children[idx]
        current_word = path + ch

        if next_node.valid_word and len(current_word) >= 3:
            found.add(current_word)

        visited.add((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                dfs(nr, nc, next_node, current_word, visited)

        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "", set())

    return list(found)


if __name__ == "__main__":
    dictionary = [
        "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape",
        "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay",
        "Race", "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"
    ]

    board1 = [
        ['A', 'D', 'E'],
        ['R', 'C', 'P'],
        ['L', 'A', 'Y']
    ]

    result1 = boggle(board1, dictionary)
    print("Board 1 results:", sorted(result1))

    print("Empty board:", boggle([], dictionary))

    board2 = [['Z', 'Z'], ['Z', 'Z']]
    print("No matches:", boggle(board2, dictionary))

    # Time spent: 40 minutes