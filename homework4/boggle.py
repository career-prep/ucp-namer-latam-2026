# Technique: Trie as a parameter
# Time: O(N * 8^L)
# Space: O(total dictionary characters)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.validWord = False


def buildTrie(dictionary):
    root = TrieNode()
    for word in dictionary:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.validWord = True
    return root


def findWords(board, dictionary):
    root = buildTrie(dictionary)
    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node, path, visited):
        char = board[r][c]
        if char not in node.children:
            return
        node = node.children[char]
        path = path + char
        if node.validWord and len(path) >= 3:
            found.add(path)

        visited.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if (dr or dc) and 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, node, path, visited)
        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "", set())
    return found


# assume a cell can't be reused in one word and order doesn't matter
dictionary = ["ace", "ape", "cape", "clap", "clay", "gape", "grape", "lace",
              "lap", "lay", "mace", "map", "may", "pace", "pay", "race", "rap",
              "ray", "tap", "tape", "trace", "trap", "tray", "yap"]
board = [["a", "d", "e"],
         ["r", "c", "p"],
         ["l", "a", "y"]]
print(sorted(findWords(board, dictionary)))

# Time spent: ~40 minutes