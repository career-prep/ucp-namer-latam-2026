class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def index(self, char):
        return ord(char.lower()) - ord('a')

    def insert(self, word):
        node = self.root

        for char in word:
            idx = self.index(char)

            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            node = node.children[idx]
        node.validWord = True
        return

    def isValidWord(self, word):
        node = self.root
        
        for char in word:
            idx = self.index(char)

            if node.children[idx] is None:
                return False
            
            node = node.children[idx]

        return node is not None and node.validWord

    def remove(self, word):
        
        def helper(node, depth):
            if node is None:
                return False

            if depth == len(word):
                if not node.validWord:
                    return False
                node.validWord = False

            else:
                idx = self.index(word[depth])
                child = node.children[idx]
                if helper(child, depth+1):
                    node.children[idx] = None

            if node is not self.root:
                c = any(child is not None for child in node.children)
                if not c and not node.validWord:
                    return True
            return False

        helper(self.root, 0)

    def print_trie(self) -> None:
        print("root")
        self._print_helper(self.root, "")

    def _print_helper(self, node: 'TrieNode', prefix: str) -> None:
        # Gather all non-None children with their letters
        entries = [
            (chr(ord('a') + i), child)
            for i, child in enumerate(node.children)
            if child is not None
        ]

        for i, (ch, child) in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            marker = " ✓" if child.validWord else ""
            print(prefix + connector + ch + marker)

            # Extend the prefix for the next level:
            # if this was the last branch, no vertical line continues
            extension = "    " if is_last else "│   "
            self._print_helper(child, prefix + extension)

#testcases
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")
trie.print_trie()

print(trie.isValidWord("cat"))  # True
print(trie.isValidWord("ca"))   # False (not marked as a word)

trie.remove("cat")
print(trie.isValidWord("cat"))  # False
print(trie.isValidWord("car"))  # True (untouched, shares prefix "ca")