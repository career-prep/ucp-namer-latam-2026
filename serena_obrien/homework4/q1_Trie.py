class TrieNode:
    def __init__(self, validWord = False):
        self.children = [None] * 26
        self.validWord = validWord

class Trie:
    def __init__(self, root: TrieNode = None):
        self.root = root

    def insert(self, word: str):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                new_node = TrieNode()
                curr.children[idx] = new_node

            curr = curr.children[idx]

        curr.validWord = True
        return
    
    def isValidWord(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None: return False
            curr = curr.children[idx]

        return curr.validWord
    
    def isEmpty(self, root: TrieNode):
        for i in range(26):
            if root.children[i]: return False
        return True
    
    def remove(self, root, word: str, depth = 0) -> TrieNode:
        if not root: return None

        if depth == len(word):
            if root.validWord:
                root.validWord = False
            if self.isEmpty(root):
                del root
                root = None
            
            return root
            
        idx = ord(word[depth]) - ord('a')
        root.children[idx] = self.remove(root.children[idx], word, depth + 1)

        if self.isEmpty(root) and not root.validWord:
            del root
            root = None
        
        return root
    
    def delete(self, word: str):
        self.root = self.remove(self.root, word)
    
if __name__ == "__main__":
    trie = Trie(TrieNode())

    words = ["cat", "car", "dog", "dart", "doggy"]

    print("Inserting words...")
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")

    print("\nChecking valid words...")
    test_words = ["cat", "car", "can", "dog", "dart", "do"]

    for word in test_words:
        result = trie.isValidWord(word)
        print(f"{word}: {result}")

    print("\nRemoving words...")
    words_to_remove = ["car", "dog"]

    for word in words_to_remove:
        trie.delete(word)
        print(f"Removed: {word}")

    print("\nChecking words after removal...")
    for word in test_words:
        result = trie.isValidWord(word)
        print(f"{word}: {result}")