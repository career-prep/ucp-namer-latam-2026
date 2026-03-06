def BackspaceStringCompare(string1, string2):

    '''
    Backward two pointer

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''

    i=len(string1)-1
    j=len(string2)-1

    skip_S=0
    skip_T=0

    while i>=0 or j>=0:
        while i>=0:
            if string1[i] == "#":
                skip_S+=1
                i-=1
            elif skip_S>0:
                skip_S-=1
                i-=1
            else:
                break

        while j>=0:
            if string2[j] == "#":
                skip_T+=1
                j-=1
            elif skip_T>0:
                skip_T-=1
                j-=1
            else:
                break
        
        if string1[i] != string2[j]:
            return False
        
        i-=1
        j-=1

    return True

# Time taken: 40mins

# string1= "Uber Career Prep"
# string2 = "u#Uber Careee#r Prep"
# output= "True"

# string1 = "abcde"
# string2 = "eerde"
# Output = False

# print(BackspaceStringCompare(string1, string2))

            
