#Time Complexity: O(N), Space Complexity: O(N)


from collections import Counter

def k_anagrams(str1, str2, k):
    freq_str1 = Counter(str1)
    freq_str2 = Counter(str2)
    
    for char in freq_str1:
        k -= freq_str1[char] - freq_str2.get(char, 0)
    
    return k >= 0




def test_cases():
    assert k_anagrams('', '', 2) == True
    assert k_anagrams('apple', 'peach', 1) == False
    assert k_anagrams("apple", 'peach', 2) == True
    assert k_anagrams("debit curd", "bad credit", 1) == True
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")
    

#time spent: 15 mins