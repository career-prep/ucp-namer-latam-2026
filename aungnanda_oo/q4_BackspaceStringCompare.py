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

# Feedback addressed by Aung for Eri
def BackspaceStringCompare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    skip_s = 0
    skip_t = 0

    while i >= 0 or j >= 0:

        # find next valid char in s
        while i >= 0:
            if s[i] == '#':
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i -= 1
            else:
                break  # found valid char

        # find next valid char in t
        while j >= 0:
            if t[j] == '#':
                skip_t += 1
                j -= 1
            elif skip_t > 0:
                skip_t -= 1
                j -= 1
            else:
                break  # found valid char

        # compare current valid chars
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            # one string still has chars, other is exhausted
            return False

        i -= 1
        j -= 1

    return True


test_cases = [
    ("abcde", "abcde"),
    ("Uber Career Prep", "u#Uber Careee#r Prep"),
    ("abcdef###xyz", "abcw#xyz"),
    ("abcdef###xyz", "abcdefxyz####")
]

for s, t in test_cases:
    print(BackspaceStringCompare(s, t))


# Time Complexity = O(n)
# Space Complexity = O(1)