# Hashing Technique. Two string increment/decrement hashmap counts
# O(n) Time Complexity where greatest length of the strings
# O(m) Space Complexity where m is the greatest number of unique characters

s1 = "apple"
s2 = "peach"
k1 = 1
k2 = 2

s3 = "cat"
s4 = "dog"
k3 = 3

s5 = "debit curd"
s6 = "bad credit"

s7 = "baseball"
s8 = "basketball"


def KAnagrams(str1, str2, k):

    # Remove whitespace
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Make sure both strings have equal length now
    if len(str1) != len(str2):
        return False
    
    # Both strings have same length if we get to this point
    n = len(str1)

    # Each hashmap will count the frequences of str1 and str2 respectively
    freq1 = {}
    freq2 = {}

    totalDiff = 0

    # Populate hashmaps
    for i in range(n):
        freq1[str1[i]] = 1 + freq1.get(str1[i], 0)
        freq2[str2[i]] = 1 + freq2.get(str2[i], 0)


    # In order to get a valid KAnagram, we need the "extra" chars of str1 to not exceed k, so we need to find our how many extra/different chars str1 has
    for key in freq1:

        totalDiff += max(freq1[key] - freq2.get(key, 0), 0)

        if totalDiff > k:
            return False
        
    return True




print(KAnagrams(s1, s2, k1))
print(KAnagrams(s1, s2, k2))
print(KAnagrams(s3, s4, k3))
print(KAnagrams(s5, s6, k1))
print(KAnagrams(s7, s8, k2))

# 29 minutes