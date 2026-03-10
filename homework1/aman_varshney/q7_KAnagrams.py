# spent 30 min
# two strings increment/decrement hashmap counts
# Time Complexity - O(n)
# Space Complexity - O(n)



def KAnagrams(s1, s2, k):
    # null cases 
    if k < 0: return False 
    if len(s1) != len(s2): return False # must be same size
    
    # load frequency maps
    freq1 = {}
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in s2:
        if char in freq1 and freq1[char] > 0:
            freq1[char] -= 1
    
    changes_needed = sum(freq1.values()) # total changes needed to make s2 an anagram of s1
    return (changes_needed <= k)
    



if __name__ == "__main__":
    input_strings = [
        ("apple", "peach"),
        ("apple", "peach"),
        ("cat", "dog"), 
        ("debit curd", "bad credit"),
        ("baseball", "basketball")
    ]
    input_ks = [
        1,
        2,
        3,
        1,
        2
    ]
    expected = [
        False,
        True,
        True,
        True,
        False
    ]
    
    for i in range(len(input_strings)):
        print("strings: ", input_strings[i][0], ", ", input_strings[i][1])
        print("k: ", input_ks[i])
        print("expected: ", expected[i])
        print("actual: ", KAnagrams(input_strings[i][0], input_strings[i][1], input_ks[i]))
        print()
        
        