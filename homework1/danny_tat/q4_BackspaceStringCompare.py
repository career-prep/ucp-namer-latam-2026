# time: O(n)
# space: O(n)
"""
Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented
by the '#' character so 'x#' results in a empty string(")

examples:
Input Strings: "abcde", "abcde"
Output: True

Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
Output: True

Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True

Input Strings: "abcdef###xyz", "abcdefxyz###"
Output: False

"""


def backspace(str1, str2):
    n = len(str1)
    m = len(str2)
    stack = []
    stack2 = []

    for i in range(n):
        if str1[i] == '#':
            if stack:
                stack.pop()
        else:
            stack.append(str1[i])

    for i in range(m):
        if str2[i] == '#':
            if stack2:
                stack2.pop()
        else:
            stack2.append(str2[i])

    return "".join(stack) == "".join(stack2)


print(backspace("abcde", "abcde"))
print(backspace("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backspace("abcdef###xyz", "abcw#xyz"))
print(backspace("abcdef###xyz", "abcdefxyz###"))

# time: 15 minutes
