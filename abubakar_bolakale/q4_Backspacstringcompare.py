""" 
Given two strings representing series of keystrokes, determine whether the resulting text is the same.
Backspaces are represented by the "#" character so "x#" results in the empty string ("").
"""
# Using stack, i keep adding into the stack.
# if the letter I am about to add is "#", i will pop the last added letter in the stack and i won't add the "#"
# return the element in stack of string1 == stack of string2

#Time complexity O(n + m)
#Space Complexity O(n + m)
class Solution():
    def backspace(self, string1, string2):
        def build(string):
            stack = []
            for i in range(len(string)):
                if stack and string[i] == "#":
                    stack.pop()
                else:
                    stack.append(string[i])
            return stack
            
        return build(string1) == build(string2)

sol = Solution()
tests = [
    ("abcde", "abcde"),
    ("Uber Career Prep", "u#Uber Careee#f Prep"),
    ("abcde####xyz", "abcw#xyz"),
    ("abcde####xyz", "abcdefxyzz###"),
    ("", ""),
    ("####", ""),
    ("a####", ""),
    ("#a#b#c#", ""),
    ("a##b", "b"),
    ("bxj##tw", "bxo#j##tw"),
]

sol = Solution()
for s1, s2 in tests:
    print(s1, s2, sol.backspace(s1, s2))
    
# 20 mins time spent