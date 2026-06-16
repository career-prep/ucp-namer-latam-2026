class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:   
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word.lower():
            index = ord(char) - ord('a')
            
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
        
        curr.isEndOfWord = True
    
    def isValidWord(self, word):
        curr = self.root

        for char in word.lower():
            index = ord(char) - ord('a')

            if curr.children[index] is None:
                return False
            
            curr = curr.children[index]
        
        return curr.isEndOfWord
    
    def remove(self, word):
        curr = self.root
        path = []

        for char in word.lower():
            index = ord(char) - ord('a')

            if curr.children[index] is None:
                return False
            
            path.append((curr, index))
            curr = curr.children[index]

        if curr.isEndOfWord == False:
            return False
        
        curr.isEndOfWord = False

        for parent, index in reversed(path):
            child = parent.children[index]

            if child.isEndOfWord:
                break

            has_child = False
            for next_node in child.children:
                if next_node is not None:
                    has_child = True
                    break
            
            if has_child:
                break

            parent.children[index] = None
    
        return True
# trie1 = Trie()

# trie1.insert("cat")

# print(trie1.isValidWord("cat"))  # True

# trie1.remove("cat")

# print(trie1.isValidWord("cat"))  # False

# trie2 = Trie()

# trie2.insert("cat")

# print(trie2.isValidWord("cat"))  # True
# print(trie2.isValidWord("cut"))  # False

# trie2.remove("cat")

# print(trie2.isValidWord("cat"))  # False
# print(trie2.isValidWord("cut"))  # False