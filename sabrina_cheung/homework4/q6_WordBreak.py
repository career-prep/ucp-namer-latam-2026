# Method: Trie
# Space Complexity: O(M * L + N)
# Time Complexity: O(N * L)
# Total Time Taken: 40 mins
# Build a trie ds for the dictionary. Using the trie iterate through each letter of the input word and check whether it is a valid word.
# If the word is valid start again and check whether the following is valid. If reached the end then the word is valid. 
# Otherwise, go back and see if there is a longer prefix that can allow the word to become valid.


class Node():
    def __init__(self):
        self.children = {}
        self.validWord = False

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.validWord = True

    def isValidWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.validWord

def WordBreak(dictionary, input):
    trie = Trie()
    input = input.lower()

    for word in dictionary:
        trie.insert(word.lower())

    DP = [False] * (len(input) + 1)

    DP[0] = True

    for i in range(len(input)):
        if DP[i]:
            cur = trie.root
            for j in range(i, len(input)):
                char = input[j]
                
                if char not in cur.children:
                    break
                    
                cur = cur.children[char]
                
                if cur.validWord:
                    DP[j + 1] = True

    return DP[len(input)]

dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
print(WordBreak(dictionary, "mangolf"))
print(WordBreak(dictionary, "manateenotelf"))
print(WordBreak(dictionary, "quipig"))
print(WordBreak(dictionary, ""))
print(WordBreak(dictionary, "teego"))