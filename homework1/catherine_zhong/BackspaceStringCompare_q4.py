#time complexity: O(n)
#space complexity: O(1)

def BackspaceStringCompare(str1, str2):
    #checks if strings are same
    if str1 == str2:
        return True

    #pointers for two strings
    str2Ptr = len(str2)-1
    str1Ptr = len(str1)-1
    skip1 = 0
    skip2 = 0

    #loops through both strings and checks if characters are identical
    while str2Ptr >= 0 or str1Ptr >= 0:
        while str1Ptr >= 0:
            if str1[str1Ptr] == '#':
                str1Ptr -= 1
                skip1 += 1
            elif skip1 > 0:
                skip1 -= 1
                str1Ptr -= 1
            else:
                break

        while str2Ptr >= 0:
            if str2[str2Ptr] == '#':
                str2Ptr -= 1
                skip2 += 1
            elif skip2 > 0:
                skip2 -= 1
                str2Ptr -= 1
            else:
                break
        
        if str1Ptr >= 0 and str2Ptr >= 0:
            if str1[str1Ptr] != str2[str2Ptr]:
                return False
        elif str1Ptr >= 0 or str2Ptr >= 0:
            return False
            
        str1Ptr -= 1
        str2Ptr -= 1
    
    return True

test1A = 'abcde'
test1B = 'abcde'
test2A = 'Uber Career Prep'
test2B = 'u#Uber Careee#r Prep'
test3A = 'abde#c'
test3B = 'abdec'
test4A = 'a#'
test4B = ''
test5A = 'bc#'
test5B = ''

print('test1: ', BackspaceStringCompare(test1A, test1B))
print('test2: ', BackspaceStringCompare(test2A, test2B))
print('test3: ', BackspaceStringCompare(test3A, test3B))
print('test4: ', BackspaceStringCompare(test4A, test4B))
print('test5: ', BackspaceStringCompare(test5A, test5B))

#time spent: 20 min