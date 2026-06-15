class TrieNode:
    def __init__(self):
        self.children = [None] * 26  
        self.valid_word = False      


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_index(self, char):
        return ord(char.lower()) - ord('a')

    def insert(self, word):
        node = self.root
        for char in word:
            idx = self._char_index(char)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.valid_word = True
        

    def is_valid_word(self, word):
        node = self.root
        for char in word:
            idx = self._char_index(char)
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.valid_word
    

    def remove(self, word):
        def _remove(node, word, depth):
            if node is None:
                return False, False
            if depth == len(word):
                if not node.valid_word:
                    return False, False
                node.valid_word = False
                return True, all(c is None for c in node.children)
            idx = self._char_index(word[depth])
            found, should_delete = _remove(node.children[idx], word, depth + 1)
            if should_delete:
                node.children[idx] = None
                return found, not node.valid_word and all(c is None for c in node.children)
            return found, False
        _remove(self.root, word, 0)


if __name__ == "__main__":
    trie = Trie()

    trie.insert("ace")
    trie.insert("ape")
    trie.insert("cape")
    trie.insert("cap")

    print(trie.is_valid_word("ace")) # True
    print(trie.is_valid_word("ape")) # True
    print(trie.is_valid_word("ap"))  # False 
    print(trie.is_valid_word("cape")) # True
    print(trie.is_valid_word("cap")) # True
    print(trie.is_valid_word("xyz")) # False

    trie.remove("cap")
    print(trie.is_valid_word("cap")) # False 
    print(trie.is_valid_word("cape")) # True 

    trie.remove("cape")
    print(trie.is_valid_word("cape")) # False

    # Time spent: 40 minutes