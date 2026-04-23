from collections import Counter
def kAnagrams(s1, s2, k):
    """
    # Technique used: two strings increment hashmap counts

    # Idea:
    count characters in both strings. The min number of replacements needed
    in s1 to make it an anagram of s2 is the sum of surpluses:
        sum(max(0, count1[ch] - count2[ch]))
    return whether that number is <= k

    # Complexity:
    Time: O(n)
    Space: O(n)

    # Time spent: 30mins
    """
    if len(s1) != len(s2):
        return False
    
    count1 = Counter(s1)
    count2 = Counter(s2)

    count = 0
    for ch, c in count1.items():
        if c > count2[ch]:
            count += c - count2[ch]
    
    return count <= k

s11, s12, k1 = "apple", "peach", 1
print(kAnagrams(s11, s12, k1))

s21, s22, k2 = "apple", "peach", 2
print(kAnagrams(s21, s22, k2))

s31, s32, k3 = "cat", "dog", 3
print(kAnagrams(s31, s32, k3))

s41, s42, k4 = "debit curd", "bad credit", 1
print(kAnagrams(s41, s42, k4))

s51, s52, k5 = "baseball", "basketball", 2
print(kAnagrams(s51, s52, k5))
