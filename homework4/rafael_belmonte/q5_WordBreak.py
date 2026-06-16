# Technique: Dynamic programming - tabulation
# time complexity: O(n^2)
# space complexity: O(n)

def word_break(s, dictionary):
    words = set(word.lower() for word in dictionary)
    s = s.lower()
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]

#test cases
dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note",
              "Pig", "Quip", "Tee", "Teen"]

assert word_break("mangolf", dictionary) == True
assert word_break("manateenotelf", dictionary) == True
assert word_break("quipig", dictionary) == False
assert word_break("", dictionary) == True

# edge cases
assert word_break("ELFgo", dictionary) == True
assert word_break("teenote", dictionary) == True
assert word_break("notetee", dictionary) == True
assert word_break("notebook", dictionary) == False
assert word_break("aaaaaaa", ["a", "aa", "aaa"]) == True
assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

print("yay!!")

# Time spent: ~20 minutes
