"""
Technique Used: Two strings increment/decrement counts
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Input: 2 strings and 1 integer k
# Output: True/false boolean
# Approach: First check if the strings are the same length, otherwise immediately False.
# Then, store the frequencies of each char in str1 and compare the frequencies of each char
# in str2 to see if they match. For all the letters that don't match, store them in a
# difference count and compare that count to k. If less than or equal to k, return True.
# Edge cases: str1 and str2 length don't match

def k_anagrams(str1: str, str2: str, k: int) -> bool:
    if len(str1) != len(str2):
        return False
    
    char_counts = {}
    for char in str1:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    for char in str2:
        if char in char_counts and char_counts[char] > 0:
            char_counts[char] -= 1

    difference_count = 0
    for count in char_counts.values():
        difference_count += count
    
    return True if difference_count <= k else False

print(k_anagrams("apple","peach",1))
print(k_anagrams("apple","peach",2))
print(k_anagrams("cat","dog",3))
print(k_anagrams("debit curd","bad credit",1))
print(k_anagrams("baseball","basketball",2))

# Time Spent: 13 minutes