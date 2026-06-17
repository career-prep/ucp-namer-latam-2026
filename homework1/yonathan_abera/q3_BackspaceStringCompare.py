#Two String, Two Pointer
#O(n) time, O(1) space
def backspace_compare(string1, string2):
    p1 = len(string1) - 1
    p2 = len(string2) - 1

    while p1 >= 0 and p2 >=0:
        if string1[p1] == string2[p2]:
            p1 -= 1
            p2 -= 1
        elif string1[p1] == "#":
            p1 -= 2
        elif string2[p2] == "#":
            p2 -= 2
        else:
            return False
    return True

print(backspace_compare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backspace_compare("ab#c", "ad#c"))    
print(backspace_compare("ab##", "c#d#"))      
print(backspace_compare("a#c", "b"))          
print(backspace_compare("a##c", "#a#c"))      
print(backspace_compare("xy#z", "xzz#"))      
print(backspace_compare("abc#d", "acc#c"))    
print(backspace_compare("", "")) 

#20 minutes