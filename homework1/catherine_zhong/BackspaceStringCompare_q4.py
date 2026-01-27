#time complexity: O(n)
#space complexity: O(n)

def BackspaceStringCompare(str1, str2):
    if str1 == str2:
        return True

    str2Ptr = len(str2)-1
    str1Ptr = len(str1)-1

    while str2Ptr >= 0 and str1Ptr >= 0:
        if str1[str1Ptr] == '#':
            str1Ptr -= 2
        if str2[str2Ptr] == '#':
            str2Ptr -= 2
        
        if str1Ptr >= 0 and str2Ptr >= 0 and str1[str1Ptr] != '#' and str2[str2Ptr] != '#':
            if str1[str1Ptr] != str2[str2Ptr]:
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

print('test1: ', BackspaceStringCompare(test1A, test1B))
print('test2: ', BackspaceStringCompare(test2A, test2B))
print('test3: ', BackspaceStringCompare(test3A, test3B))
print('test4: ', BackspaceStringCompare(test4A, test4B))

#time spent: 20 min