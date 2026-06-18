# spent 45 minutes
# Trie as parameter
# TC - O(n^2)
# SC - O(n) 

from q1_BuildTrie import Trie, TrieNode


def boggle(dictionary: set, board: list[list[str]]) -> set:
    """Returns all valid words according to Boggle rules given a board and list of accepted words"""
    # Load trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word.upper())

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    rows = cols = len(board)
    result = set()

    # helper
    def dfs(r: int, c: int, node: TrieNode, path: str, visited: set) -> None:
        """Explores different directions for `path` if in accordance with `trie`"""
        # Out of bounds / already visited base case
        if (r < 0 or r >= rows or c < 0 or c >= cols) or ((r, c) in visited):
            return

        # Update pointers
        char = board[r][c].upper() 
        if char not in node.children: # Path DNE in trie
            return
        node = node.children[char]
        path += char 
        
        # Add to output list if valid
        if node.valid_word and len(path) >= 3:
            result.add(path)

        # Explore adjacent letters in board
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r+dr, c+dc, node, path, visited)
        visited.remove((r, c))


    # Explore each path in board
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "", set())

    return result


def run_tests():
    print("Running tests")
    
    dictionary = (
        "Ace", "Ape", "Cape", "Clap", "Clay", "Race", "Rap", "Ray",
        "Gape", "Grape", "Lace", "Lap", "Lay", "Tap", "Tape", "Trace",
        "Mace", "May", "Pace", "Pay", "Trap", "Tray", "Yap"
    )
    board = [
        ["A", "D", "E"],
        ["R", "C", "P"],
        ["L", "A", "Y"]
    ]
    expected = {
        "ACE", "RACE", "PACE", "LACE", "PAY",
        "LAY", "CLAY", "RAY", "LAP", "RAP",
        "CLAP", "APE", "CAPE", "YAP"
    }

    actual = boggle(dictionary, board)
    assert actual == expected
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()