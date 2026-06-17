class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.valid_word = True

    def is_valid_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.valid_word

    def remove(self, word):
        def delete_helper(node, index):
            if index == len(word):
                if not node.valid_word:
                    return False

                node.valid_word = False
                return len(node.children) == 0

            char = word[index]

            if char not in node.children:
                return False

            should_delete_child = delete_helper(
                node.children[char],
                index + 1
            )

            if should_delete_child:
                del node.children[char]

            return (
                len(node.children) == 0
                and not node.valid_word
            )

        delete_helper(self.root, 0)


def Test_Trie():
    trie = Trie()

    trie.insert("cat")
    trie.insert("car")
    trie.insert("care")
    trie.insert("dog")

    print(trie.is_valid_word("cat"))   # True
    print(trie.is_valid_word("car"))   # True
    print(trie.is_valid_word("care"))  # True
    print(trie.is_valid_word("dog"))   # True
    print(trie.is_valid_word("ca"))    # False
    print(trie.is_valid_word("cow"))   # False

    trie.remove("cat")

    print(trie.is_valid_word("cat"))   # False
    print(trie.is_valid_word("car"))   # True
    print(trie.is_valid_word("care"))  # True

    print(trie.is_valid_word("care"))  # False
    print(trie.is_valid_word("car"))   # True

    trie.remove("car")

    print(trie.is_valid_word("car"))   # False
    print(trie.is_valid_word("dog"))   # True


if __name__ == "__main__":
    Test_Trie()