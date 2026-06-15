def word_break(s, dictionary):

    s = s.lower()
    word_set = set(w.lower() for w in dictionary)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

    print(word_break("mangolf", dictionary))       # True  
    print(word_break("manateenotelf", dictionary)) # True  
    print(word_break("quipig", dictionary))        # False

    # Time spent: 40 mintes