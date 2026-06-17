# Technique: Dynamic programming (tabulation) with Trie as a parameter
# Time Complexity: O(n^2) + O(dictionary chars)
# Space Complexity: O(n) + O(dictionary chars)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def build_trie(dictionary):
    root = TrieNode()
    for w in dictionary:
        node = root
        for ch in w.lower():
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True
    return root


def word_break(s, dictionary):
    s = s.lower()
    root = build_trie(dictionary)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        if not dp[i]:
            continue
        node = root
        for j in range(i, n):
            if s[j] not in node.children:
                break
            node = node.children[s[j]]
            if node.is_word:
                dp[j + 1] = True
    return dp[n]

dictionary = [
    "Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note",
    "Pig", "Quip", "Tee", "Teen",
]
print(word_break("mangolf", dictionary))
print(word_break("manateenotelf", dictionary))
print(word_break("quipig", dictionary))
print(word_break("", dictionary))
print(word_break("xyz", dictionary))

# Time spent:70
