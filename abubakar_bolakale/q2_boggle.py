class BoggleTrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""

def insert_word(root: BoggleTrieNode, word: str) -> None:
    curr = root
    for char in word:
        index = ord(char.lower()) - ord('a')
        if not curr.children[index]:
            curr.children[index] = BoggleTrieNode()
        curr = curr.children[index]
    curr.word = word

def dfs(board: list[list[str]], r: int, c: int, node: BoggleTrieNode, visited: list[list[bool]], result: set[str]) -> None:
    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or visited[r][c]:
        return

    ch = board[r][c].lower()
    index = ord(ch) - ord('a')
    if not node.children[index]:
        return

    node = node.children[index]
    if len(node.word) >= 3:
        result.add(node.word)

    visited[r][c] = True
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        dfs(board, r + dr[i], c + dc[i], node, visited, result)
        
    visited[r][c] = False

def find_words(board: list[list[str]], dictionary: list[str]) -> list[str]:
    root = BoggleTrieNode()
    for word in dictionary:
        insert_word(root, word)

    rows = len(board)
    if rows == 0:
        return []
    cols = len(board[0])

    result_set = set()
    visited = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            dfs(board, r, c, root, visited, result_set)

    return sorted(list(result_set))


if __name__ == "__main__":
    dictionary = [
        "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay",
        "Mace", "Map", "May", "Pace", "Pay", "Race", "Rap", "Ray", "Tap", "Tape",
        "Trace", "Trap", "Tray", "Yap"
    ]
    board = [
        ['A', 'D', 'E'],
        ['R', 'C', 'P'],
        ['L', 'A', 'Y']
    ]

    res = find_words(board, dictionary)
    assert len(res) == 14

    assert find_words([], dictionary) == []
    assert find_words([['A']], dictionary) == []

    single_board = [['C', 'A', 'T']]
    single_dict = ["Cat", "At", "Ca"]
    assert find_words(single_board, single_dict) == ["Cat"]

    no_match_board = [['X', 'Y', 'Z']]
    assert find_words(no_match_board, dictionary) == []

    dup_dict = ["Ace", "Ace", "ace"]
    dup_res = find_words(board, dup_dict)
    assert len(dup_res) == 1
    assert dup_res[0].lower() == "ace"

    two_letter_dict = ["At", "To", "Go"]
    two_letter_board = [['A', 'T'], ['O', 'G']]
    assert find_words(two_letter_board, two_letter_dict) == []

    print("All Boggle tests passed!")
