# Technique: Two array two pointer
# Runtime: O(n)
# Space complexity: O(n + m)

def BackspaceStringCompare(word1, word2):
    chars1 = list(word1)
    chars2 = list(word2)
    n1 = len(chars1)
    n2 = len(chars2)
    pointer1 = n1-1
    pointer2 = n2-1
    while pointer1 > 0 and pointer2 > 0:
        delCount = 0
        while pointer1 > 0 and chars1[pointer1] == '#':
            delCount +=1
            pointer1 -=1
        while delCount > 0:
            pointer1 -= 1
            delCount -= 1

        while pointer2 > 0 and chars2[pointer2] == '#':
            delCount +=1
            pointer2 -=1
        while delCount > 0:
            pointer2 -= 1
            delCount -= 1
        if chars1[pointer1] != chars2[pointer2]:
            return False
        pointer1 -= 1
        pointer2 -= 1
    return True




print(BackspaceStringCompare("abcde", "abcde") == True)
print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep") == True)
print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz") == True)
print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###") == False)




# Time spent: 15:30
