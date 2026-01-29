# Question 4: BackspaceStringCompare

# Given two strings representing series of keystrokes, determine whether the resulting text is the same.
# Backspaces are represented by the "#" character so "x#" results in the empty string ("").

# Examples:

# Input Strings: "abcde", "abcde"
# Output: True

# Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
# Output: True

# Input Strings: "abcdef###xyz", "abcw#xyz"
# Output: True

# Input Strings: "abcdef###xyz", "abcdefxyz####"
# Output: False

def clean_string(s):
    i = len(s) - 1
    skip = 0
    result = []

    while i >= 0:
        if s[i] == '#':
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            result.append(s[i])   # keep valid character
        i -= 1

    return "".join(reversed(result))


def BackspaceStringCompare(s,t):

    clean_S = clean_string(s)
    clean_T = clean_string(t)

    return clean_S == clean_T


test_cases = [("abcde", "abcde"),("Uber Career Prep", "u#Uber Careee#r Prep"),("abcdef###xyz", "abcw#xyz"), ("abcdef###xyz", "abcdefxyz####")]

for test_case in test_cases:
    s, t = test_case
    print(BackspaceStringCompare(s,t))

# Time Complexity = O(n)
# Space Complexity = O(n)

# Spent a total of 40 mins on this question