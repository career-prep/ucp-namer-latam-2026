"""
Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.
"""

from math import inf
class Solution:
    def shortestsubstring(self, string1, string2):
        if not string2:
            return 0
        if not string1:
            return -1

        need = {}
        for ch in string2:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        required = len(need)
        formed = 0

        best = float("inf")
        left = 0

        for right in range(len(string1)):
            ch = string1[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            
    
tests = [
    ("abracadabra", "abc"),
    ("zxycbaabcdwzyzzxwdcbyzabcobazyx", "zzyzx"),
    ("dog", "god"),
    ("", ""),
    ("", "a"),
    ("a", ""),
    ("aaaaa", "aa"),
    ("aaaaa", "b"),
    ("abc", "abcd"),
    ("ab", "b"),
    ("ab", "a"),
    ("aabbcc", "abc"),
    ("aabbcc", "aabc"),
    ("ADOBECODEBANC", "ABC"),
    ("aAaAaA", "Aa"),
    ("abc", "cba"),
    ("abcbcba", "abbc"),
    ("the quick brown fox", "qbf"),
    ("####", "##"),
    ("a#b#c#", "a"),
]

sol = Solution()
for s1, s2 in tests:
    print(s1, s2, sol.shortestsubstring(s1, s2))
    
#40 mins spent