#Technique: Two strings two pointer

#Time Complexity: O(n + m), both string 1 and string 2
#Space Complexity: O(1)

def BackspaceStringCompress(str1, str2):
    l = len(str1) - 1
    r = len(str2) - 1
    skip1 = 0
    skip2 = 0

    while l >= 0 or r >= 0:
        while l >= 0:
            if str1[l] == '#':
                skip1 += 1
                l -= 1
            elif skip1 > 0:
                skip1 -= 1
                l -= 1
            else:
                break

        while r >= 0:
            if str2[r] == '#':
                skip2 += 1
                r -= 1
            elif skip2 > 0:
                skip2 -= 1
                r -= 1
            else:
                break
    
        if l >= 0 and r >= 0:
            if str1[l] != str2[r]:
                return False
        
        l -= 1
        r -= 1

    return True

print(BackspaceStringCompress("abcde", "abcde"))
print(BackspaceStringCompress("Uber Career Prep", "u#Uber Careee#r Prep"))
print(BackspaceStringCompress("abcdef###xyz", "abcw#xyz"))     
print(BackspaceStringCompress("abcdef###xyz", "abcdefxyz###")) 

#Time taken: 32 min 
    

        


