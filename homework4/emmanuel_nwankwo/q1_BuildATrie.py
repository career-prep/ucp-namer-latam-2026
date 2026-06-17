class TrieNode:
    def __init__(self):
        self.validWord = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        length = len(word)

        for i in range(length):
            index = ord(word[i]) - ord('a')

            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]

        curr.validWord = True

    def isValidWord(self, word):
        if word == "":
            return False

        curr = self.root

        for i in range(len(word)):
            index = ord(word[i]) - ord("a")
            curr = curr.children[index]

            if curr is None:
                return False

        return curr.validWord

    def isEmpty(self, root):
        for i in range(len(root.children)):
            if root.children[i] is not None:
                return False

        return True

    def remove(self, word):
        self.remove_helper(self.root, word, 0)

    def remove_helper(self, root:TrieNode, word, i=0):
        if not root:
            return None

        if i == len(word):
            if root.validWord:
                root.validWord = False
            if self.isEmpty(root):
                root = None
            return root

        index = ord(word[i]) - ord("a")
        root.children[index] = self.remove_helper(root.children[index], word, i + 1)

        if self.isEmpty(root) and not root.validWord:
            root = None

        return root

# Time Taken: 18mins 32secs
if __name__ == "__main__":
    # Test Case:
    trie = Trie()

    trie.insert("cat")
    trie.insert("car")
    trie.insert("dog")

    print(trie.isValidWord("cat"))
    print(trie.isValidWord("car"))
    print(trie.isValidWord("dog"))
    print(trie.isValidWord("cow"))

    trie.remove("cat")

    print(trie.isValidWord("cat"))
    print(trie.isValidWord("car"))
    print(trie.isValidWord("dog"))