"""
Given two strings and an integer k, determine if the strings are k-anagrams.
Two strings are k-anagrams if they can become anagrams by changing at most k characters.

Examples:
Input: "apple", "peach", k=1 -> Output: False
Input: "debit curd", "bad credit", k=1 -> Output: True
"""

def kAnagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
    
    changes_needed = 0
    
    for char in freq1:
        if char in freq2:
            if freq1[char] > freq2[char]:
                changes_needed += freq1[char] - freq2[char]
        else:
            changes_needed += freq1[char]
    
    return changes_needed <= k

# Time Complexity: O(n)
# Space Complexity: O(1) - bounded by alphabet size


test_cases = [
    ("apple", "peach", 1),
    ("debit curd", "bad credit", 1)
]

for s1, s2, k in test_cases:
    print(kAnagrams(s1, s2, k))
