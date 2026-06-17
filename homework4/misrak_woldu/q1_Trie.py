# Data Structure: Trie
# Algorithms: Insert, Search, Delete
# Time Complexity:
# - insert: O(word length)
# - is_valid_word: O(word length)
# - remove: O(word length)
# Space Complexity: O(total characters stored in trie)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        current_node.valid_word = True

    def is_valid_word(self, word: str) -> bool:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.valid_word

    def remove(self, word: str) -> None:
        self._remove_helper(self.root, word, 0)

    def _remove_helper(self, current_node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            if not current_node.valid_word:
                return False

            current_node.valid_word = False

            return len(current_node.children) == 0

        char = word[index]

        if char not in current_node.children:
            return False

        child_node = current_node.children[char]
        should_delete_child = self._remove_helper(child_node, word, index + 1)

        if should_delete_child:
            del current_node.children[char]

            return len(current_node.children) == 0 and not current_node.valid_word

        return False


def run_tests() -> None:
    trie = Trie()

    # insert and search normal words
    trie.insert("cat")
    trie.insert("car")
    trie.insert("dog")

    assert trie.is_valid_word("cat") is True
    assert trie.is_valid_word("car") is True
    assert trie.is_valid_word("dog") is True

    # prefix should not count as a full word unless inserted
    assert trie.is_valid_word("ca") is False
    assert trie.is_valid_word("do") is False

    # word not in trie
    assert trie.is_valid_word("cow") is False

    # removing one word should not remove shared prefix words
    trie.remove("cat")
    assert trie.is_valid_word("cat") is False
    assert trie.is_valid_word("car") is True

    # removing a word that is not present should not break the trie
    trie.remove("cow")
    assert trie.is_valid_word("car") is True
    assert trie.is_valid_word("dog") is True

    # word that is prefix of another word
    trie.insert("app")
    trie.insert("apple")

    assert trie.is_valid_word("app") is True
    assert trie.is_valid_word("apple") is True

    trie.remove("app")
    assert trie.is_valid_word("app") is False
    assert trie.is_valid_word("apple") is True

    # removing longer word should keep shorter word if it exists
    trie.insert("app")
    trie.remove("apple")
    assert trie.is_valid_word("apple") is False
    assert trie.is_valid_word("app") is True

    # empty string support
    trie.insert("")
    assert trie.is_valid_word("") is True
    trie.remove("")
    assert trie.is_valid_word("") is False

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
