#Samaksh Arora
#Question 1 - Build a Trie
#Data Structure Implementation
#Time Complexity:
#Space Complexity:
#Time Spent:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isValidWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        pass

    def search(self, word):
        pass

    def delete(self, word):
        pass


#Test Cases
# trie = Trie()
# trie.insert("cat")
# trie.insert("car")
# trie.insert("card")
# assert trie.search("cat") == True
# assert trie.search("ca") == False
# assert trie.search("car") == True
# trie.delete("cat")
# assert trie.search("cat") == False
# assert trie.search("car") == True
# assert trie.search("card") == True

# Extra: trie.insert("dog"), trie.insert("doggo")
# assert trie.search("dog") == True
# assert trie.search("doggo") == True
# trie.delete("dog")
# assert trie.search("dog") == False
# assert trie.search("doggo") == True
