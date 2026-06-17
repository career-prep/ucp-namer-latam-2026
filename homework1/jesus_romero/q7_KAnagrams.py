"""
Time, Space complexities: O(n), O(1)
Q7: KAnagrams
Two strings are considered to be k anagrams if they can be made into anagrams by changing
at most k characters in one of the strings. Given two strings and an integer k, determine
if they are k anagrams
"""


def KAnagrams(s1, s2, k):
    # 1. Length check remains mandatory
    if len(s1) != len(s2):
        return False
    
    # 2. Fixed-size list (26 zeros for a-z)
    char_counts = [0] * 26
    
    # 3. Increment for the first string
    for char in s1:
        index = ord(char) - ord('a')
        char_counts[index] += 1
        
    # 4. Decrement for the second string
    # We only care about characters in s2 that "cancel out" s1
    for char in s2:
        index = ord(char) - ord('a')
        if char_counts[index] > 0:
            char_counts[index] -= 1
            
    # 5. Sum the remaining positive counts
    # This represents characters in s1 that were NOT found in s2
    changes_needed = sum(char_counts)
    
    return changes_needed <= k

def test_KAnagrams():
    input_strings = ("apple", "peach")
    k = 1
    expected = False
    result = KAnagrams(input_strings[0], input_strings[1], k)
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("apple", "peach")
    k = 2
    expected = True
    result = KAnagrams(input_strings[0], input_strings[1], k)
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("cat", "dog")
    k = 3
    expected = True
    result = KAnagrams(input_strings[0], input_strings[1], k)
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("debitcurd", "badcredit")
    k = 1
    expected = True
    result = KAnagrams(input_strings[0], input_strings[1], k)
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("baseball", "basketball")
    k = 2
    expected = False
    result = KAnagrams(input_strings[0], input_strings[1], k)
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_KAnagrams()