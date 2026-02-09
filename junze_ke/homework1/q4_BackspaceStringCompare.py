# Time: 40 Minutes 
# Techique: backwards 2 pointers 
def BackspaceStringCompare(a,b):
    a1 = list(a)
    b1 = list(b)

    l = 0
    r = len(a1) - 1

    l1 = 0
    r1 = len(b1) - 1

    while l < r and l1 < r1:
        if l1 < r1 and b1[r1] == "#":
            r1-=2
        elif l < r and a1[r] == "#":
            r-=2
        else:
            if b1[r1] != a1[r]:
                return False
            else:
                r1-=1
                r-=1
    return True

print(BackspaceStringCompare("abcde","abcde")) #True
print(BackspaceStringCompare("Uber Career Prep","u#Uber Careee#r Prep")) #True
print(BackspaceStringCompare("abcdef###xyz","abcdefxyz###")) #False
