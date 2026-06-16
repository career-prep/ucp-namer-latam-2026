# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n^3)
# Space Complexity: O(n)

def word_break(s, words):
    words = set(word.lower() for word in words)

    dp = [False] * (len(s) + 1)
    dp[0] = True

    s = s.lower()
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]

# Time Taken: 17mins 9secs

# Testcases:
dictionary_1 = [
    "Elf",
    "Go",
    "Golf",
    "Man",
    "Manatee",
    "Not",
    "Note",
    "Pig",
    "Quip",
    "Tee",
    "Teen"
]

string_1 = "mangolf"
print(word_break(string_1, dictionary_1))

string_2 = "manateenotelf"
print(word_break(string_2, dictionary_1))

string_3 = "quipig"
print(word_break(string_3, dictionary_1))

#Edge cases:
string_4 = "" # Empty string
print(word_break(string_4, dictionary_1))

string_5 = "man" # One word
print(word_break(string_5, dictionary_1))