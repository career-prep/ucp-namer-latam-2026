from q1_Trie import Trie
# Implementation time: 30 min

def boggle(board, dictionary):
    #1. Declare variables
    trie = Trie()
    result = set()
    rows = len(board)
    cols = len(board[0])

    #2. Build trie
    for word in dictionary:
        if len(word) >= 3:
            trie.insert(word.lower())

    def dfs(row, col, node, path, visited):
        #1. Check bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        #2. Check visited
        if (row, col) in visited:
            return

        char = board[row][col].lower()

        #3. Check trie path
        if char not in node.children:
            return

        node = node.children[char]
        path += char
        visited.add((row, col))

        #4. Save valid word
        if node.valid_word:
            result.add(path)

        #5. Search neighbors
        for r_move in [-1, 0, 1]:
            for c_move in [-1, 0, 1]:
                if r_move != 0 or c_move != 0:
                    dfs(row + r_move, col + c_move, node, path, visited)

        #6. Backtrack
        visited.remove((row, col))

    #3. Search from each cell
    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie.root, "", set())

    return list(result)


def Test_Boggle():
    dictionary = [
        "Ace", "Ape", "Cape", "Clap", "Clay",
        "Gape", "Grape", "Lace", "Lap", "Lay",
        "Mace", "Map", "May", "Pace", "Pay",
        "Race", "Rap", "Ray", "Tap", "Tape",
        "Trace", "Trap", "Tray", "Yap"
    ]

    board = [
        ["A", "D", "E"],
        ["R", "C", "P"],
        ["L", "A", "Y"]
    ]

    words = boggle(board, dictionary)

    print("Words found:")
    for word in sorted(words):
        print(word)


if __name__ == "__main__":
    Test_Boggle()