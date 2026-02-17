# Technique: Two strings increment/decrement count
# Runtime: O(n)
# Space complexity: O(n + m)

from collections import Counter


def KAnagrams(word1, word2, k):
    if len(word1) != len(word2):
       return False # assuming words have to be the same length in order to be anagrams. Can switch a char to ""
    counts1 = Counter(word1)
    counts2 = Counter(word2)
    for char in counts1:
      if counts2.get(char, 0) != counts1.get(char,0):
         k -= abs(counts2[char] - counts1[char])
    return k >= 0



print(KAnagrams("apple", "peach", 1) == False)
print(KAnagrams("apple", "peach", 2) == True)
print(KAnagrams("cat", "dog", 3) == True)
print(KAnagrams("debit curd", "bad credit", 1) == True)
print(KAnagrams("baseball", "basketball", 2) == False)
# Time spent: 25:00, 40:00
# I'm assuming there is a way to do it with one hashmap but I couldn't figure it out.
