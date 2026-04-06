#Two strings increment hash counts
#O(n) time, O(n) space
#Assumption:
#Changing does not consitute removing a character
#No Empty strings
from collections import defaultdict
def k_anagrams(string1, string2, k):
    if len(string1) != len(string2):
        return False
    hash1 = defaultdict(int)
    hash2 = defaultdict(int)

    for s in string1:
        hash1[s] += 1
    for s in string2:
        hash2[s] += 1

    difference = 0
    for char in hash1:
        difference += abs(hash1.get(char, 0) - hash2.get(char, 0))
    if difference <= k:
        return True
    else:
        return False
print(k_anagrams("apple", "peach", 2))
print(k_anagrams("anagram", "grammar", 3))
print(k_anagrams("anagram", "mangaar", 0))
print(k_anagrams("apple", "pepla", 2))
print(k_anagrams("abcd", "dcba", 0))
print(k_anagrams("abcd", "abcf", 1))
print(k_anagrams("abcd", "abcf", 0))

# 26 minutes 