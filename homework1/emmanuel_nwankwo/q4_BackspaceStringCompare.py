# Technique: Forward/backward two-pointer
# Time Complexity: O(N + M)
# Space Complexity: O(1)

def compare(str1, str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    count1 = 0  # number of characters to skip in str1 due to backspaces
    count2 = 0  # number of characters to skip in str2 due to backspaces

    while p1 >= 0 or p2 >= 0:
        # Move p1 to the next valid character in str1
        while p1 >= 0:
            if str1[p1] == "#":
                count1 += 1
                p1 -= 1
            elif count1 > 0:
                count1 -= 1
                p1 -= 1
            else:
                break  # str1[p1] is valid

        # Move p2 to the next valid character in str2
        while p2 >= 0:
            if str2[p2] == "#":
                count2 += 1
                p2 -= 1
            elif count2 > 0:
                count2 -= 1
                p2 -= 1
            else:
                break  # str2[p2] is valid

        # Compare current valid characters
        ch1 = str1[p1] if p1 >= 0 else None
        ch2 = str2[p2] if p2 >= 0 else None
        if ch1 != ch2:
            return False

        p1 -= 1
        p2 -= 1

    return True

print(compare("abcde", "abcde"))
print(compare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(compare("abcdef###xyz", "abcw#xyz"))
print(compare("abcdef###xyz", "abcdefxyz###"))

# My Edge Testcases:
print(compare("", "")) # empty strings
print(compare("####", "")) # only backspaces
print(compare("ab##", "c#d#")) # both become empty

# Time Taken: 9mins 21secs
