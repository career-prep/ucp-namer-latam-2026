# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Two arrays/strings two-pointer

def BackSpaceStringCompare(str1, str2):
    p1, p2 = len(str1)-1, len(str2)-1

    while p1 >= 0 or p2 >= 0:
        
        backspaceCounter1 = 0
        while p1 >= 0:
            if str1[p1] == '#':
                backspaceCounter1 += 1
                p1 -= 1
            elif backspaceCounter1 > 0:
                p1 -= 1
                backspaceCounter1 -=1
            else:
                break

        backspaceCounter2 = 0
        while p2 >= 0:
            if str2[p2] == '#':
                backspaceCounter2 += 1
                p2 -= 1
            elif backspaceCounter2 > 0:
                p2 -= 1
                backspaceCounter2 -=1
            else:
                break 

        if p1 >= 0 and p2 >= 0:
            if str1[p1] != str2[p2]:
                return False
            
        elif p1 >= 0 or p2 >= 0:
            return False
        
        p1 -= 1
        p2 -= 1

    return True
        
if __name__ == '__main__':
    # inputStr1 = "abcde"
    # inputStr2 = "abcde"
    # inputStr1 = "Uber Career Prep"
    # inputStr2 = "u#Uber Careee#r Prep"
    inputStr1 = "###"
    inputStr2 = "#####"
    # inputStr1 = ""
    # inputStr2 = ""
    print("Input Strings:", inputStr1, ',', inputStr2)
    print("Output:", BackSpaceStringCompare(inputStr1, inputStr2))

# ~ time spent: 20 minutes