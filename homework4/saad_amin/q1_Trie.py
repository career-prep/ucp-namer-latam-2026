class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_word = True

    def is_valid_word(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_word

    def remove(self, word):
        def delete_helper(node, index):
            if index == len(word):
                if not node.is_word:
                    return False

                node.is_word = False

                return len(node.children) == 0

            char = word[index]

            if char not in node.children:
                return False

            should_delete_child = delete_helper(
                node.children[char], index + 1
            )

            if should_delete_child:
                del node.children[char]

                return (
                    not node.is_word and
                    len(node.children) == 0
                )

            return False

        delete_helper(self.root, 0)