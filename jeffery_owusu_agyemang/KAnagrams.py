# Question 7 ()
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 25 mins


from collections import Counter

def kAnagrams(s, t, k):
    if len(s) != len(t):
        return False

    count_s = Counter(s)
    count_t = Counter(t)

    changes = 0

    for char in count_s:
        if count_s[char] > count_t.get(char, 0):
            changes += count_s[char] - count_t.get(char, 0)

    return changes <= k



#Tests
print(kAnagrams("anagram", "grammar", 3))  # True
print(kAnagrams("apple", "peach", 1))      # False
print(kAnagrams("apple", "appel", 0))      # True
print(kAnagrams("abcd", "abcd", 0))        # True
