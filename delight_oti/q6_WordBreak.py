# Technique: Dynamic programming - Tabulation
def WordBreak(word, dictionary):

    dp = [False] * (len(word) + 1)

    dp[0] = True

    for end in range(1, len(word) + 1):

        for start in range(end):

            current_word = word[start:end].lower()

            if dp[start] and current_word in dictionary:
                dp[end] = True
                break
    return dp[len[word]]

# dictionary = {
#     "elf", "go", "golf", "man",
#     "manatee", "not", "note", "pig",
#     "quip", "tee", "teen"
# }

# print(WordBreak("mangolf", dictionary))
# Output: True

# print(WordBreak("manateenotelf", dictionary))
# Output: True

# print(WordBreak("quipig", dictionary))
# Output: False