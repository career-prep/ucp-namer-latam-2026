# Question 6: WordBreak

# Technique: Dynamic programming (tabulation)
# dp[i] = True if s[:i] can be segmented into valid dictionary words.
# dp[0] = True (empty prefix is trivially valid).
# For each position i, check all words: if dp[i - len(w)] is True and
# s[i-len(w):i] == w.lower(), then dp[i] = True.

# Assumption: dictionary matching is case-insensitive.

# Time Complexity:  O(n * W * L) where n = len(s), W = dict size, L = max word
# Space Complexity: O(n)


def wordBreak(s, dictionary):
    s = s.lower()
    words = {w.lower() for w in dictionary}
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for word in words:
            wlen = len(word)
            if i >= wlen and dp[i - wlen] and s[i - wlen:i] == word:
                dp[i] = True
                break
    return dp[n]
# Time Complexity = O(n * W * L), Space Complexity = O(n)


# --- Tests ---

dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

print("'mangolf':", wordBreak("mangolf", dictionary))           # True
print("'manateenotelf':", wordBreak("manateenotelf", dictionary))  # True
print("'quipig':", wordBreak("quipig", dictionary))             # False
print("'golf':", wordBreak("golf", dictionary))                 # True
print("'teen':", wordBreak("teen", dictionary))                 # True
print("'teennote':", wordBreak("teennote", dictionary))         # True
print("'xyz':", wordBreak("xyz", dictionary))                   # False
print("'':", wordBreak("", dictionary))                         # True (empty string)

# Spent a total of 25 mins on this question
