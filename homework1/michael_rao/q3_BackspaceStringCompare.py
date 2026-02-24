# method: two strings two pointer
# time: O(n)
# space: O(1)

def backspaceStringCompare(str1, str2):
    p1 = len(str1)-1
    p2 = len(str2)-1
    while p1 >= 0 and p2 >= 0:
        s1Del = 0
        while str1[p1] == '#':
            p1 -= 1
            s1Del += 1
        p1 -= s1Del
        s2Del = 0
        while str2[p2] == '#':
            p2 -= 1
            s2Del += 1
        p2 -= s2Del
        if str1[p1] != str2[p2]:
            return False
        p1 -= 1
        p2 -= 1
    return True

def checkSolution(str1, str2, correct):
    print("Input Strings:", str1, ",", str2)
    print("Correct:", correct)
    print("Output: ", backspaceStringCompare(str1, str2))
    print()

checkSolution("abcde","abcde",True)
checkSolution("Uber Career Prep","u#Uber Careee#r Prep",True)
checkSolution("abcdef###xyz","abcw#xyz",True)
checkSolution("abcdef###xyz","abcdefxyz###",False)

# time taken: 9 min