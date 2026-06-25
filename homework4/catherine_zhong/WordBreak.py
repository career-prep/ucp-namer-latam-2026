#trie and dynamic programming
#time complexity: O(n^2)
# space complexity: O(n)

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


def WordBreak(dictionary, str):
    #if empty string return false
    if not str:
        return False

    words = Trie()

    for i in dictionary:
        words.insert(i)

    table = [False] * len(str)

    table[0] = words.isValidWord(str[0])

    for i in range(len(str)):
        if words.isValidWord(str[0:i+1]):
            table[i] = True
        for j in range(i):
            table[i] = table[i] or (table[j] and words.isValidWord(str[j+1:i+1]))

    return table[-1]

#test cases
dictionary = ['Elf', 'Go', 'Golf', 'Man', 'Manatee', 'Not', 'Note', 'Pig', 'Quip', 'Tee', 'Teen']

input = 'mangolf'
print(WordBreak(dictionary, input))

input2 = 'manateenotelf'
print(WordBreak(dictionary, input2))

input3 = 'quipig'
print(WordBreak(dictionary, input3))
