"""
40 minutes
time complexity O(n)
space complexity O(n0)

"""

def substring(str1, str2):
    dic1 = {}
    dic2 = {}
    for ch in str2:
        if ch in dic2:
            dic2[ch] += 1
        else:
            dic2[ch] = 1
    left = 0
    for right in range (len(str1)):
        if str1[right] in dic2:





str1 = "abracadabra"
str2 = "abc"

print(substring(str1, str2))
