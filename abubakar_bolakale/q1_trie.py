class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.validWord = True

    def isValidWord(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr is not None and curr.validWord

    def _has_children(self, node: TrieNode) -> bool:
        return any(child is not None for child in node.children)

    def _remove_helper(self, curr: TrieNode, word: str, depth: int) -> TrieNode:
        if not curr:
            return None

        if depth == len(word):
            if curr.validWord:
                curr.validWord = False
            if not self._has_children(curr):
                del curr
                curr = None
            return curr

        index = ord(word[depth]) - ord('a')
        curr.children[index] = self._remove_helper(curr.children[index], word, depth + 1)

        if not self._has_children(curr) and not curr.validWord:
            del curr
            curr = None

        return curr

    def remove(self, word: str) -> None:
        self.root = self._remove_helper(self.root, word, 0)
        if not self.root:
            self.root = TrieNode()


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    assert trie.isValidWord("apple") == True
    assert trie.isValidWord("app") == False

    trie.insert("app")
    assert trie.isValidWord("app") == True

    trie.remove("apple")
    assert trie.isValidWord("apple") == False
    assert trie.isValidWord("app") == True

    trie.remove("app")
    assert trie.isValidWord("app") == False

    assert trie.isValidWord("") == False
    trie.insert("a")
    trie.remove("a")
    assert trie.isValidWord("a") == False

    trie.insert("cat")
    trie.insert("car")
    trie.insert("card")
    assert trie.isValidWord("car") == True
    assert trie.isValidWord("card") == True
    trie.remove("car")
    assert trie.isValidWord("car") == False
    assert trie.isValidWord("card") == True
    assert trie.isValidWord("cat") == True

    trie.remove("xyz")
    assert trie.isValidWord("xyz") == False

    trie.insert("dog")
    trie.remove("dog")
    trie.insert("dog")
    assert trie.isValidWord("dog") == True

    print("All Trie tests passed!")
