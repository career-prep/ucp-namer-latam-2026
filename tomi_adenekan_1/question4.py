"""
two pointer
20 minutes
"""
def check(str):
    i = len(str) - 1
    while i >= 0 and  str[i] == '#':
        i -= 1
    return i

def get_name(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1

    while i >= 0 and j >= 0:
        if str1[i] == "#" and str2[j] == "#":
            i = check(str1[:i])
            j = check(str2[:j])
        elif str1[i] == '#':
            i = check(str1[:i])
        else:
            j = check(str2[:j])

        if str1[i] != str2[j]:
            return False
        j -= 1
        i -= 1

    return True





str1 = "abcdef###xyz"
str2 = "abcw#xyz"

print(get_name(str1, str2))
    
