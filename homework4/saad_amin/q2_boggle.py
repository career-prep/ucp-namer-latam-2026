# Technique: Trie 
# Time Complexity: O(R * C)
# Space Complexity O(R * C)

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        
class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        current = self.root

        for char in word.lower():
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]

        current.is_word = True
        current.word = word


def solve_boggle(board, dictionary):
    trie = Trie()

    for word in dictionary:
        if len(word) >= 3:
            trie.add_word(word)

    rows = len(board)
    cols = len(board[0])
    found_words = set()

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def explore(row, col, current_node, used):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        if (row, col) in used:
            return

        letter = board[row][col].lower()

        if letter not in current_node.children:
            return

        next_node = current_node.children[letter]

        if next_node.is_word:
            found_words.add(next_node.word)

        used.add((row, col))

        for row_change, col_change in directions:
            explore(
                row + row_change,
                col + col_change,
                next_node,
                used
            )

        used.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            explore(row, col, trie.root, set())

    return found_words


def main():
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

    result = solve_boggle(board, dictionary)

    print("Words found:", sorted(result))

    print("Ace found:", "Ace" in result)
    print("Clay found:", "Clay" in result)
    print("Cat found:", "Cat" in result)


if __name__ == "__main__":
    main()
    
#Time 35 min