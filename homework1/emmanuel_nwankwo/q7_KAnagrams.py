# Technique: Two arrays/strings increment/decrement hashmap counts
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter

def k_anagrams(str1, str2, k):
    # Different lengths can never be anagrams
    if len(str1) != len(str2):
        return False

    count_str1 = Counter(str1) # frequency of chars in str1
    count_str2 = Counter(str2) # frequency of chars in str2
    changes = 0

    # Count how many extra chars in str1 must be changed
    for char in count_str1:
        if count_str1[char] > count_str2.get(char, 0):
            changes += count_str1[char] - count_str2.get(char, 0)

    # Check if required changes are qual or less than k
    return changes <= k

print(k_anagrams("apple", "peach", 1))
print(k_anagrams("apple", "peach", 2))
print(k_anagrams("cat", "dog", 3))
print(k_anagrams("debit curd", "bad credit", 1))
print(k_anagrams("baseball", "basketball", 2))

# My Edge Testcases:
print(k_anagrams("", "", 0)) # both empty
print(k_anagrams("a", "a", 0)) # already an anagram

# Time Taken: 8mins 26secs

