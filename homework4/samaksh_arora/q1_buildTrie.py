#Samaksh Arora
#Question 1 - Build a Trie
#Data Structure Implementation
#Time Complexity: O(M) for insert, isValidWord, and remove where M is the length of the word
#Space Complexity: O(1) for operations; O(ALPHABET_SIZE * N * M) for total trie storage where N is number of words
#Time Spent: >40 minutes


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False
        self.idx = -1
        self.refs = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx=-1):
        currentNode = self.root
        currentNode.refs += 1
        for char in word:
            index = ord(char) - ord('a')
            if currentNode.children[index] is None:
                currentNode.children[index] = TrieNode()

            currentNode = currentNode.children[index]
            currentNode.refs += 1

        currentNode.validWord = True
        currentNode.idx = idx

    def isValidWord(self, word):
        currentNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            if currentNode.children[index] is None:
                return False

            currentNode = currentNode.children[index]

        return currentNode.validWord

    def remove(self, word):
        def deleteHelper(node, word, index):
            if index == len(word):
                if not node.validWord:
                    return False
                node.validWord = False
                return not any(node.children)

            char = word[index]
            charIndex = ord(char) - ord('a')
            if node.children[charIndex] is None:
                return False

            shouldDeleteChild = deleteHelper(node.children[charIndex], word, index + 1)

            if shouldDeleteChild:
                node.children[charIndex] = None
                return not any(node.children) and not node.validWord

            return False
        deleteHelper(self.root, word, 0)


#Test Cases
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("card")
assert trie.isValidWord("cat") == True
assert trie.isValidWord("ca") == False
assert trie.isValidWord("car") == True
trie.remove("cat")
assert trie.isValidWord("cat") == False
assert trie.isValidWord("car") == True
assert trie.isValidWord("card") == True

#Extra: 
trie.insert("dog"), trie.insert("doggo")
assert trie.isValidWord("dog") == True
assert trie.isValidWord("doggo") == True
trie.remove("dog")
assert trie.isValidWord("dog") == False
assert trie.isValidWord("doggo") == True
