# Technique: Dynamic programming
# Time Complexity: O(n * m * k)
# Space Complexity: O(n)

def word_break(s, word_dict):
    s = s.lower()
    word_dict = [word.lower() for word in word_dict]

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:
            if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                dp[i] = dp[i + len(word)]

            if dp[i]:
                break

    return dp[0]


def main():
    word_dict = [
        "Elf", "Go", "Golf", "Man",
        "Manatee", "Not", "Note", "Pig",
        "Quip", "Tee", "Teen"
    ]

    print(word_break("mangolf", word_dict))      # True
    print(word_break("manateenot", word_dict))   # True
    print(word_break("mangopig", word_dict))     # True


if __name__ == "__main__":
    main()
    
#Time: 39 min