# Two Pointers: Backward Two Pointer
# O(m) Time complexity where m is the length of the longer string
# O(1) Space Complexity

s1, s2 = "abcde", "abcde"

s3, s4 = "Uber Career Prep", "u#Uber Careee#r Prep"

s5, s6 = "abcdef###xyz", "abcw#xyz"

s7, s8 = "abcdef###xyz", "abcdefxyz###"

def BackSpaceStringCompare(str1, str2):

    # Start Scanning from the end of each string. If we encounter a '#', we can skip the char it corresponds to

    p1 = len(str1) - 1
    p2 = len(str2) - 1

    # Keep scanning until both pointers are done
    while p1 >= 0 or p2 >= 0:

        # Make sure that both pointers end up on a valid char

        # Counts how many times we need to skip
        skip1 = 0
        skip2 = 0

        while p1 >= 0:
            if str1[p1] == '#':
                skip1 += 1
                p1 -= 1
            elif skip1 > 0:
                skip1 -= 1
                p1 -= 1
            else:
                # Now p1 is on a valid char
                break

        # Do the same for p2
        while p2 >=0: 
            if str2[p2] == '#':
                skip2 += 1
                p2 -= 1
            elif skip2 > 0:
                skip2 -= 1
                p2 -= 1
            else:
                break

        
        
        # If p1 and p2 are valid indices and are on valid characters, compare them
        if p1 >= 0 and p2 >= 0:
            if str1[p1] != str2[p2]:
                return False
        else:
            # One string is done being processed while the other still has more to process
            if p1 >= 0 or p2 >= 0:
                return False
            
        # Keep scanning
        p1 -= 1
        p2 -= 1



    return True


print(BackSpaceStringCompare(s1, s2))
print(BackSpaceStringCompare(s3, s4))
print(BackSpaceStringCompare(s5, s6))
print(BackSpaceStringCompare(s7, s8))

# 34 minutes
