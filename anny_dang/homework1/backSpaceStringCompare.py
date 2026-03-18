def compareBlackSpaceStrings(s1, s2):
    """
    # Technique used: Stack 

    # Idea:
    use a stack to build the final string after applying blackspaces 
    - if the character is "#", pop from the stack if it is empty 
    - otherwise, push the character onto the stack 
    
    # Complexity:
    Time: O(m + n)
    Space: O(m + n)

    # Time spent: 15mins
    """
    def simplify(s):
        stack = []
        for i in range(len(s)):
            if s[i] == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        
        return stack 

    return simplify(s1) == simplify(s2)

s11, s12 = "abcde", "abcde"
print(compareBlackSpaceStrings(s11, s12))

s21, s22 = "Uber Career Prep", "u#Uber Careee#r Prep"
print(compareBlackSpaceStrings(s21, s22))

s31, s32 = "abcdef###xyz", "abcw#xyz"
print(compareBlackSpaceStrings(s31, s32))

s41, s42 = "abcdef###xyz", "abcdefxyz###"
print(compareBlackSpaceStrings(s41, s42))

