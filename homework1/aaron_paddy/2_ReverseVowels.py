def reverse_vowels(word):
    word_list = list(word)
    vowels = 'aeiou'
    l = 0
    r = len(word) - 1
    
    while l < r:
        if word_list[l].lower() in vowels and word_list[r].lower() in vowels:
            temp = word_list[l]
            word_list[l], word_list[r] = word_list[r], temp
            l += 1
            r -= 1
        elif word_list[l].lower() in vowels and word_list[r].lower() not in vowels:
            r -= 1
        elif word_list[l].lower() not in vowels and word_list[r].lower() in vowels:
            l += 1
        else:
            l += 1
            r -= 1
            
    return "".join(word_list)



def test_cases():
    assert reverse_vowels('') == ''
    assert reverse_vowels("Uber Career Prep") == "eber Ceraer PrUp"
    assert reverse_vowels("xyz") == "xyz"
    assert reverse_vowels("flamingo") == "flominga"
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")