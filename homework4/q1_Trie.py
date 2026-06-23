class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.valid_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _has_no_children(self, node: TrieNode) -> bool:
        return all(child is None for child in node.children)

    def _remove_helper(self, curr: TrieNode, word: str, depth: int) -> TrieNode:
        if curr is None:
            return None

        if depth == len(word):
            if curr.valid_word:
                curr.valid_word = False

            if self._has_no_children(curr):
                curr = None

            return curr

        index = ord(word[depth]) - ord('a')
        curr.children[index] = self._remove_helper(curr.children[index], word, depth + 1)

        if self._has_no_children(curr) and not curr.valid_word:
            curr = None

        return curr

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.valid_word = True

    def isValidWord(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.valid_word

    def remove(self, word: str) -> None:
        self.root = self._remove_helper(self.root, word, 0)