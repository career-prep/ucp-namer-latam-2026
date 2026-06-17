# Technique: Trie as a parameter + DFS backtracking
# Data Structure: Trie / Matrix
# Time Complexity: O(rows * cols * 8^L), where L is the max word length
# Space Complexity: O(total dictionary characters + rows * cols)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word.lower():
            if char not in current_node.children:
                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        current_node.word = word


def find_boggle_words(board: list[list[str]], dictionary: list[str]) -> list[str]:
    if not board or not board[0] or not dictionary:
        return []

    trie = Trie()

    for word in dictionary:
        if len(word) >= 3:
            trie.insert(word)

    row_count = len(board)
    col_count = len(board[0])
    found_words = set()
    visited_cells = set()

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    def dfs(row_index: int, col_index: int, current_node: TrieNode) -> None:
        if (
            row_index < 0
            or row_index >= row_count
            or col_index < 0
            or col_index >= col_count
            or (row_index, col_index) in visited_cells
        ):
            return

        current_char = board[row_index][col_index].lower()

        if current_char not in current_node.children:
            return

        next_node = current_node.children[current_char]

        if next_node.word is not None:
            found_words.add(next_node.word)

        visited_cells.add((row_index, col_index))

        for row_change, col_change in directions:
            dfs(row_index + row_change, col_index + col_change, next_node)

        visited_cells.remove((row_index, col_index))

    for row_index in range(row_count):
        for col_index in range(col_count):
            dfs(row_index, col_index, trie.root)

    return sorted(found_words)


def run_tests() -> None:
    dictionary = [
        "Ace", "Ape", "Cape", "Clap", "Clay",
        "Gape", "Grape", "Lace", "Lap", "Lay",
        "Mace", "Map", "May", "Pace", "Pay",
        "Race", "Rap", "Ray", "Tap", "Tape",
        "Trace", "Trap", "Tray", "Yap",
    ]

    board = [
        ["A", "D", "E"],
        ["R", "C", "P"],
        ["L", "A", "Y"],
    ]

    expected_words = {
        "Ace", "Race", "Pace", "Lace", "Pay",
        "Lay", "Clay", "Ray", "Lap", "Rap",
        "Clap", "Ape", "Cape", "Yap",
    }

    assert set(find_boggle_words(board, dictionary)) == expected_words

    # empty board
    assert find_boggle_words([], dictionary) == []

    # empty dictionary
    assert find_boggle_words(board, []) == []

    # words shorter than 3 should not be returned
    small_dictionary = ["A", "An", "Ace"]
    small_board = [
        ["A", "C"],
        ["E", "X"],
    ]

    assert find_boggle_words(small_board, small_dictionary) == ["Ace"]

    # cannot reuse the same board position in one word
    reuse_board = [
        ["A", "B"],
        ["C", "D"],
    ]

    reuse_dictionary = ["ABA"]
    assert find_boggle_words(reuse_board, reuse_dictionary) == []

    # diagonal movement is allowed
    diagonal_board = [
        ["C", "X"],
        ["X", "A"],
        ["X", "T"],
    ]

    diagonal_dictionary = ["Cat"]
    assert find_boggle_words(diagonal_board, diagonal_dictionary) == ["Cat"]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
    