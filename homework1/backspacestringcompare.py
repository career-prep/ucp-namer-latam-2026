'''Question 4: BackspaceStringCompare
Given two strings representing series of keystrokes, determine whether the resulting text is the same.
Backspaces are represented by the '#' character so "x#" results in the empty string ('').

Examples:
eInput Strings: "abcde", "abcde"
Output: True
Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep" Output: True
Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True
Input Strings: "abcdef##|#xyz", "abcdefxyz###"
Output: False

technique- one derectional comparing 
time- 25 min
time complexity- o(N) as it just iterates one time
'''

# def backspacestringcompare(str1, str2):
#     def cleanword(x):
#         stack = []
#         for ch in x:
#             if ch == '#':
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(ch)
#         return ''.join(stack)

#     return cleanword(str1) == cleanword(str2)

# print(backspacestringcompare("abcde", "abcde"))
# print(backspacestringcompare("abcdef##|#xyz", "abcdefxyz###"))



# after the suggestion- iterate backwards, skip characters based on backspace count
# time complexity- o(N)  space complexity- o(1)

def backspacestringcompare(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1
    skip1 = 0
    skip2 = 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if str1[i] == '#':
                skip1 += 1
                i -= 1
            elif skip1 > 0:
                skip1 -= 1
                i -= 1
            else:
                break

        while j >= 0:
            if str2[j] == '#':
                skip2 += 1
                j -= 1
            elif skip2 > 0:
                skip2 -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0 and str1[i] != str2[j]:
            return False

        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True

print(backspacestringcompare("abcde", "abcde"))
print(backspacestringcompare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backspacestringcompare("abcdef###xyz", "abcw#xyz"))
print(backspacestringcompare("abcdef##|#xyz", "abcdefxyz###"))