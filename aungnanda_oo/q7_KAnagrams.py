# Question 7: KAnagrams

# Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

# Examples:

# Input Strings: "apple", "peach"
# Input k: 1
# Output: False

# Input Strings: "apple", "peach"
# Input k: 2
# Output: True

# Input Strings: "cat", "dog"
# Input k: 3
# Output: True

# Input Strings: "debit curd", "bad credit"
# Input k: 1
# Output: True

# Input Strings: "baseball", "basketball"
# Input k: 2
# Output: False

from collections import Counter
def KAnagrams(s1, s2, k) -> bool:

    if len(s1) != len(s2):
        return False
    
    c1 = Counter(s1)
    c2 = Counter(s2)


    changes = 0
    for c in c1:
        if c1[c] > c2.get(c, 0):
            changes += c1[c] - c2.get(c, 0)

    return changes <= k

# Time Complexity: O(n)
# Space Complexity: O(n)

test_cases = [("apple", "peach",1), ("apple", "peach", 2), ("cat", "dog",3), ("debit curd", "bad credit", 1), ( "baseball", "basketball", 2) ]

for test_case in test_cases:
    s1, s2, k = test_case
    print(KAnagrams(s1, s2, k)) 

# Spent a total of 40 mins on this question