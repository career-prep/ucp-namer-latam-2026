'''
    Pointer & Hashing technique:

    Maintain 2 stack to keep track of the final transformation of the 2 strings
    For each string, tranverse over all characters
    If char is #, pop the previous char, else apppend
    Compare the final 2 stack

    Time: O(n + m)
    Space: O(n + m)
    n, m: length of the 2 given strings

    Optimize approach:
    Tranverse the array from end to beginning to check which character can be keep
    If keep the same chracter from each string each iteration, continue
    Else different string

    Time: O(n + m)
    Space: O(1)
    n, m: length of the 2 given strings

    Time spent: 40 mins
'''

def BackspaceStringCompare(a: str, b: str) -> bool:
    p1 = len(a) - 1
    p2 = len(b) - 1

    # Keep track of the backspace
    skip_a = 0
    skip_b = 0

    while p1 >= 0 or p2 >= 0:
        # Find what character is valid in a
        while p1 >= 0:
            if a[p1] == '#':
                skip_a += 1
                p1 -= 1
            elif skip_a > 0:
                skip_a -= 1
                p1 -= 1
            else:
                # Find a valid character
                break

        # Find what character is valid in b
        while p2 >= 0:
            if b[p2] == '#':
                skip_b += 1
                p2 -= 1
            elif skip_b > 0:
                skip_b -= 1
                p2 -= 1
            else:
                # Find a valid character
                break

        # Compare the valid characters
        char_a = a[p1] if p1 >= 0 else ""
        char_b = b[p2] if p2 >= 0 else ""

        if char_a != char_b:
            return False

        # Move the pointers past the validated char
        p1 -= 1
        p2 -= 1
    
    return True


a, b = "abcde", "abcde"
print(BackspaceStringCompare(a, b))
a, b = "Uber Career Prep", "u#Uber Careee#r Prep"
print(BackspaceStringCompare(a, b))
a, b = "abcdef###xyz", "abcw#xyz"
print(BackspaceStringCompare(a, b))
a, b = "abcdef###xyz", "abcdefxyz###"
print(BackspaceStringCompare(a, b))