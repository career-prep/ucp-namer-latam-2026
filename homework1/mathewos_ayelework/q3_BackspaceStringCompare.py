# Technique used: Two strings two-pointer method
# compares to see if two strings are the same, the '#' char represents backspace
def backspaceStringCompare(str1: str, str2: str) -> bool:

    p1 = len(str1) - 1
    p2 = len(str2) - 1
    counterp1, counterp2 = 0, 0

    while p1 >= 0 and p2 >= 0:
        # both str[p1] and str2[p2] are not #
        if str1[p1] != '#' and str2[p2] != '#':
            while counterp1 > 0 and p1 >= 0:
                p1-=1
                counterp1 -=1
            while counterp2 > 0 and p2 >= 0:
                p2 -= 1
                counterp2 -=1

            if str1[p1] != str2[p2]:
                return False
            p1 -= 1
            p2 -= 1
        # if str[p1] is # and str2[p2] isn't
        elif str1[p1] == '#' and str2[p2] != '#':
            counterp1 += 1
            p1 -= 1
        # if str[p1] isn't # and str2[p2] is
        elif str1[p1] != '#' and str2[p2] == '#':
            counterp2 += 1
            p2 -= 1
        # both str[p1] and str2[p2] are #  
        else:
            counterp1 += 1
            counterp2 += 1
            p1 -= 1
            p2 -= 1
    print(p1,p2)
    return True

print("backspaceStringCompare Results:")
test_cases = [
        ["abcde", "abcde"],
        ["Uber Career Prep", "u#Uber Careee#r Prep"],
        ["abcdef###xyz", "abcw#xyz"],
        ["abcdef###xyz", "abcdefxyz###"],
        ["", ""],
        ["###", "a##"] # assuming cases like this where it goes out of range, return True 
               ]
for test_case in test_cases:
    print(backspaceStringCompare(test_case[0], test_case[1])) #Expected Output: T,T,T,F,T,T

# Time Complexity: O(n)
# Space Complexity: O(1)
# Time Taken: 37mins