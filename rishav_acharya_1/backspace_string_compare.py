"""
Given two strings representing series of keystrokes, determine whether the resulting text is the same.
Backspaces are represented by the "#" character.

Examples:
Input: "abcde", "abcde" -> Output: True
Input: "Uber Career Prep", "u#Uber Careee#r Prep" -> Output: True
Input: "abcdef###xyz", "abcw#xyz" -> Output: True
Input: "abcdef###xyz", "abcdefxyz####" -> Output: False
"""

def process_string(s):
    stack = []
    
    for char in s:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)


def backspaceCompare(s, t):
    return process_string(s) == process_string(t)


test_cases = [
    ("abcde", "abcde"),
    ("Uber Career Prep", "u#Uber Careee#r Prep"),
    ("abcdef###xyz", "abcw#xyz"),
    ("abcdef###xyz", "abcdefxyz####")
]

for s, t in test_cases:
    print(backspaceCompare(s, t))
