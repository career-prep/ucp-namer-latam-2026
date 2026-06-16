# Technique: Dynamic programming (tabulation)
# dp[i] = True if text[:i] splits into dictionary words
# Time: O(n^2)
# Space: O(n)


def wordBreak(text, dictionary):
    words = set(dictionary)
    n = len(text)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and text[j:i] in words:
                dp[i] = True
                break
    return dp[n]


dictionary = ["elf", "go", "golf", "man", "manatee", "not", "note", "pig",
              "quip", "tee", "teen"]
print(wordBreak("mangolf", dictionary))        # True
print(wordBreak("manateenotelf", dictionary))  # True
print(wordBreak("quipig", dictionary))         # False

# Time spent: ~25 minutes