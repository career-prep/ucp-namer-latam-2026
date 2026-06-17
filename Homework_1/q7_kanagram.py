# Two strings are considered to be "k-anagrams" if they can be made into anagrams 
# by changing at most k characters in one of the strings. Given two strings and 
# an integer k, determine if they are k-anagrams.

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

from collections import Counter
def kAnagrams(str1,str2,k):
    if len(str1)!=len(str2): return False
    count1 = Counter(str1)
    count2 = Counter(str2)
    changes=0
    for char in count1:
        if char in count2:
            changes+=max(0,count1[char]-count2[char])
        else:
            changes+=count1[char]

    return changes<=k

print(kAnagrams("apple", "peach",2))
print(kAnagrams("apple", "peach", 1))
print(kAnagrams("cat", "dog", 3))
print(kAnagrams("debit card", "bad credit", 1))
print(kAnagrams("baseball", "basketball", 2))
print(kAnagrams("listen", "silent", 0))
print(kAnagrams("hello", "world", 4))
print(kAnagrams("abc", "def", 3))
print(kAnagrams("anagram", "nagaram", 0))
print(kAnagrams("rat", "car", 2))


#Time Complexity: O(n+m)
#Space Complexity: O(n+m)
#Spent 10 mins