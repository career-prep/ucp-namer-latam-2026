#Samaksh Arora
#Question 1 - Build a Trie
#Data Structure Implementation
#Time Complexity:
#Space Complexity:
#Time Spent:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.validWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()

            currentNode = currentNode.children[char]

        currentNode.validWord = True

    def isValidWord(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False

            currentNode = currentNode.children[char]

        return currentNode.validWord

    def remove(self, word):
        def deleteHelper(node, word, index):
            if index == len(word):
                if not node.validWord:
                    return False
                node.validWord = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            shouldDeleteChild = deleteHelper(node.children[char], word, index + 1)

            if shouldDeleteChild:
                del node.children[char]
                return len(node.children) == 0 and not node.validWord

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
