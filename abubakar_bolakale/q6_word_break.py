def word_break(s: str, word_dict: list[str]) -> bool:
    dictionary = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                break
                
    return dp[n]


if __name__ == "__main__":
    dict_words = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
    
    assert word_break("ManGolf", dict_words) == True
    assert word_break("ManateeNotElf", dict_words) == True
    assert word_break("quipig", dict_words) == False
    assert word_break("", dict_words) == True
    assert word_break("xyz", dict_words) == False

    assert word_break("Go", dict_words) == True
    assert word_break("Golf", dict_words) == True
    assert word_break("Manatee", dict_words) == True
    assert word_break("NotNote", dict_words) == True
    assert word_break("Tee", dict_words) == True

    single_dict = ["a"]
    assert word_break("a", single_dict) == True
    assert word_break("aa", single_dict) == True
    assert word_break("b", single_dict) == False

    print("All WordBreak tests passed!")
