# Technique: Forward/backward two-pointer
# Time Complexity: O(N + M)
# Space Complexity: O(1)

def compare(str1, str2):
    new_str1 = ""
    new_str2 = ""

    p1 = len(str1) - 1
    p2 = len(str2) - 1
    count1 = 0
    count2 = 0

    while p1 >= 0:
        if str1[p1] == "#":
            count1 += 1
            p1 -= 1
        elif count1 > 0:
            count1 -= 1
            p1 -= 1
        else:
            new_str1 += str1[p1]
            p1 -= 1

    while p2 >= 0:
        if str2[p2] == "#":
            count2 += 1
            p2 -= 1
        elif count2 > 0:
            count2 -= 1
            p2 -= 1
        else:
            new_str2 += str2[p2]
            p2 -= 1

    return new_str1 == new_str2

print(compare("abcde", "abcde"))
print(compare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(compare("abcdef###xyz", "abcw#xyz"))
print(compare("abcdef###xyz", "abcdefxyz###"))

# My Edge Testcases:
print(compare("", "")) # empty strings
print(compare("####", "")) # only backspaces
print(compare("ab##", "c#d#")) # both become empty

# Time Taken: 9mins 21secs
