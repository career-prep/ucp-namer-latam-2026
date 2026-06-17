# Question 6: WordBreak
# Given a string without spaces and a dictionary of valid words, determine
# whether the string can be broken into a list of valid dictionary words.

def word_break(text, dictionary):
    words = set(word.lower() for word in dictionary)
    text = text.lower()
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for end in range(1, len(text) + 1):
        for start in range(end):
            if dp[start] and text[start:end] in words:
                dp[end] = True
                break
    return dp[-1]
dictionary = [
    "Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note",
    "Pig", "Quip", "Tee", "Teen",
]


print(word_break("mangolf", dictionary))
print(word_break("manateenotelf", dictionary))
print(word_break("quipig", dictionary))
print(word_break("", dictionary))


# Spent 25 mins
# Time Complexity: O(n^2 * k), where k is substring slicing/checking length.
# Space Complexity: O(n)
