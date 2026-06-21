# technique: dynamic programming - tabulation (with trie as parameter for word lookup)
# time complexity: O(n^2 * m) where n = string length, m = avg word length
# space complexity: O(n + W*m) where W = dictionary size
# time taken: 35 mins

class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.valid_word = True

def wordBreak(s, dictionary):
    s = s.lower()
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    n = len(s)
    # dp[i] = True if s[:i] can be broken into valid words
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if not dp[j]:
                continue
            node = trie.root
            matched = True
            for k in range(j, i):
                if s[k] not in node.children:
                    matched = False
                    break
                node = node.children[s[k]]
            if matched and node.valid_word:
                dp[i] = True
                break

    return dp[n]


dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

print(wordBreak("mangolf", dictionary))         # True
print(wordBreak("manateenotelf", dictionary))   # True
print(wordBreak("quipig", dictionary))          # False
print(wordBreak("golf", dictionary))            # True
print(wordBreak("pigelf", dictionary))          # True
