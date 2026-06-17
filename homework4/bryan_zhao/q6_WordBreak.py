# Technique: Dynamic Programming (Tabulation)
# Time Complexity:
# Space Complexity:

def word_break(s: str, dictionary: list[str]) -> bool:
    word_set = set(word.lower() for word in dictionary)
    s = s.lower()

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break


    return dp[n]

dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
print(word_break("mangolf", dictionary))
print(word_break("manateenotelf", dictionary))
print(word_break("quipig", dictionary))

# Time Spent: 25 minutes