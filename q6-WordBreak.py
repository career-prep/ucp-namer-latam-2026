class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEndOfWord = True

    def isValidWord(self, word):
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEndOfWord 

    def remove(word):

        def helper(node, word, depth = 0):
            if depth == len(word):
                node.isEndOfWord = False
                return all(child is None for child in node.children)
            
            ch = word[depth]
            index = ord(ch) - ord('a')
            can_delete = helper(node.children[index], word, depth + 1)

            if can_delete:
                node.children[index] = None 
            return not node.isEndOfWord and all(child is None for child in node.children)
        
        return helper(self,word, 0)

def WordBreak(dictionary,input):
    trie = Trie()

    for word in dictionary:
        trie.insert(word.lower())
    
    dp = [False] * (len(input) + 1)
    dp[0] = True

    for i in range(1, len(input) + 1):
        for j in range(0, i):
            if dp[j] and trie.isValidWord(input[j:i]):
                dp[i] = True
    
    return dp[len(input)]
dictionary = ["Elf",
"Go",
"Golf",
"Man",
"Manatee",
"Not",
"Note",
"Pig",
"Quip",
"Tee",
"Teen"]

print(WordBreak(dictionary, 'mangolf'))

