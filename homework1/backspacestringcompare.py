# Question 4: BackspaceStringCompare
# Given two strings representing series of keystrokes, determine whether the resulting text is the same.
# Backspaces are represented by the '#' character so "x#" results in the empty string ('').

# Examples:
# eInput Strings: "abcde", "abcde"
# Output: True
# Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep" Output: True
# Input Strings: "abcdef###xyz", "abcw#xyz"
# Output: True
# Input Strings: "abcdef##|#xyz", "abcdefxyz###"
# Output: False

# technique- one derectional comparing 
# time- 25 min
# time complexity- o(N) as it just iterates one time

def backspacestringcompare(str1, str2):
    def cleanword(x):
        stack = []
        for ch in x:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    return cleanword(str1) == cleanword(str2)

print(backspacestringcompare("abcde", "abcde"))
print(backspacestringcompare("abcdef##|#xyz", "abcdefxyz###"))

