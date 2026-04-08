""" 
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k 
characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.
"""
#using hashmap
# if the lenght of the two string arem't equal, return false immidiately
# use two hashmap to store the frequency of each string.
# if the frequency of a letter is string1 is greater than the frequency of that letter in string two, increase the change.
# the aim of this is to know how many letters we can change in string1 in order to acheive string2
# return chnage

#Time complexity O(n+m)
#Space complexity O(n)
class Solution():
    def kanagrams(self, string1, string2, k):
        if len(string1) != len(string2):
            return False
        
        freq1 = {}
        freq2 = {}
        
        for ch in string1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
                
        for ch in string2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1
        
        changes = 0       
        for key, value in freq1.items():
            if key in freq2:
                value2 = freq2[key]
            else:
                value2 = 0
            
            if value > value2:    
                changes += (value - value2)
            
        return  changes <= k
        
sol = Solution()
test_cases = [
    ("apple", "peach", 1),
    ("apple", "peach", 2),
    ("cat", "dog", 3),
    ("debit curd", "bad credit", 1),
    ("baseball", "basketball", 2),

    ("", "", 0),
    ("", "", 5),
    ("a", "a", 0),
    ("a", "b", 0),
    ("a", "b", 1),

    ("ab", "ba", 0),
    ("ab", "ba", 1),

    ("aaaa", "aaaa", 0),
    ("aaaa", "bbbb", 4),
    ("aaaa", "bbbb", 3),

    ("aab", "abb", 0),
    ("aab", "abb", 1),

    ("abc", "def", 2),
    ("abc", "def", 3),

    ("abc", "ab", 1),
    ("ab", "abc", 1),

    ("a b", "ab ", 0),
    ("a b", "ab ", 1),

    ("Debit Curd", "bad credit", 2),
    ("debit curd", "bad credit", 0),

    ("listen", "silent", 0),
    ("listen", "silent", 1),

    ("x" * 50, "y" * 50, 50),
    ("x" * 50, "y" * 50, 49),
]

for string1, string2, k in test_cases:
    print(sol.kanagrams(string1, string2, k))
    
#25 min spent