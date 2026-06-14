class TrieNode:
    def __init__(self):
        self.validWord = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    

    # Add a word to the Trie in O(k) time where k is the length of the string we are trying to insert
    def insert(self, word):

        # This pointer marks the current node we are on in the path
        curr = self.root

        for char in word:

            childIndex = ord(char) - ord('a')

            if curr.children[childIndex] == None:
                curr.children[childIndex] = TrieNode()

            curr = curr.children[childIndex]

        # Mark this word as True now that we reached the end of it
        curr.validWord = True




    # Returns a boolean indicating whether 'word' is in the Trie in O(k) time where k is the length of the string we are trying to search for
    def isValidWord(self, word):

        curr = self.root

        for char in word:

            childIndex = ord(char) - ord('a')

            # If during the search, we find that we do not have nodes needed for this word, return False
            if curr.children[childIndex] == None:
                return False
            
            curr = curr.children[childIndex]


        # If we reach the end of the word, make sure that the word is a valid word in the Trie
        return curr.validWord # This is either True or False
    



    # Returns a boolean to whether this node has any children
    def isEmpty(self, node):

        for i in range(26):
            if node.children[i] != None:
                return False
            
        return True
    




    # Removes a word from the Trie and deletes unused nodes in O(k) time where k is the length of the string we are trying to delete
    # This remove function is a wrapper function for the delete function below
    def remove(self, word):

        self.root = self.delete(self.root, word, 0)



    def delete(self, node, word, k): # k is the current index of the word we are on (sometimes referred to as depth)

        if not node:
            return None
            

        if k == len(word): # We have reached the end of the word
            node.validWord = False 
            
            # If this node has no children, then delete it
            if self.isEmpty(node):
                return None
                
            return node
            

        # Recursive Step
        childIndex = ord(word[k]) - ord('a')

        node.children[childIndex] = self.delete(node.children[childIndex], word, k+1)


        # After recursion, if this node is NOT a word and has ZERO children, then delete it
        if not node.validWord and self.isEmpty(node):
            return None
            
        return node

            


                


        


    




            

