#Time: O(D*L + rows*cols*8^L) - D is dictionary size, L is max word length; DFS explores paths with prefix pruning
#Space: O(D*L + rows*cols) - stores words, prefixes, and visited cells in recursion stack

def find_words(board: list[list], dictionary: set):
    rows = len(board)
    cols = len(board[0])

    words = set(word.lower() for word in dictionary)

    prefixes = set()
    for word in words:
        for i in range(1, len(word) + 1):
            prefixes.add(word[:i])

    result = set()

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def dfs(r, c, current_word, visited):
        current_word += board[r][c].lower()

        if current_word not in prefixes:
            return

        if len(current_word) >= 3 and current_word in words:
            result.add(current_word)

        visited.add((r, c))

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
            ):
                dfs(nr, nc, current_word, visited)

        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, "", set())

    return sorted(result)

#Time-taken: 35 minutes


import unittest


class TestBoggle(unittest.TestCase):

    def test_finds_multiple_words(self):
        board = [
            ["C", "A", "T"],
            ["R", "A", "R"],
            ["D", "O", "G"],
        ]
        dictionary = {"CAT", "CAR", "RAT", "ART", "DOG", "TAR"}
        self.assertEqual(
            find_words(board, dictionary),
            ["art", "car", "cat", "dog", "rat", "tar"],
        )

    def test_returns_empty_list_when_no_words_exist(self):
        board = [
            ["X", "Y"],
            ["Z", "W"],
        ]
        dictionary = {"CAT", "DOG"}
        self.assertEqual(find_words(board, dictionary), [])

    def test_case_insensitive_dictionary(self):
        board = [
            ["C", "A", "T"],
            ["R", "A", "R"],
            ["D", "O", "G"],
        ]
        dictionary = {"cat", "Cat", "DOG"}
        self.assertEqual(find_words(board, dictionary), ["cat", "dog"])


if __name__ == "__main__":
    unittest.main()