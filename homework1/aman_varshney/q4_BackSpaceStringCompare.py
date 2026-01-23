# spent 40 min
# stacks
# Time Complexity - O(n)
# Space Complexity - O(n)

def backstringCompare(s1, s2):
    if (not s1 or not s2): # cannot be empty strings
        return None
    if (s1[0] == "#" or s2[0] == "#"): # cannot start with backslash
        return None
    
    stack1 = [] # stack for s1
    stack2 = [] # stack for s2
    
    for char in s1: 
        if char == "#": # back
            if len(stack1) == 0: # backlog
                return None
            stack1.pop()
        else:
            stack1.append(char)
        
    for char in s2:
        if char == "#": # back
            if len(stack2) == 0: # backlog
                return None
            stack2.pop()
        else:
            stack2.append(char)
            
    while stack1 and stack2:
        if stack1.pop() != stack2.pop(): # different characters
            return False
        
    if stack1 or stack2: # uneven lengths
        return False
    
    return True


'''
def backstringCompare(s1, s2):
    # null cases
    if not s1: 
        return None
    if not s2:
        return None
    
    right1 = len(s1)-1 
    skip_count1 = 0
    right2 = len(s2)-1
    skip_count2 = 0
    
    while (right1 >= 0 and right2 >= 0):
        char1 = None
        char2 = None
        
        if s1[right1] == "#":
            skip_count1 += 1
        elif skip_count1 == 0:
            char1 = s1[right1]
        else:
            skip_count1 -= 1
        
        if s2[right2] == "#":
            skip_count2 += 1
        elif skip_count2 == 0:
            char2 = s2[right2]
        else:
            skip_count1 -= 1
        
        if ((char1 and char2) and char1 != char2):
            print("diff")
            return False
        
        right1 -= 1
        right2 -= 1
        
    if not (skip_count1 == 0 and skip_count2 == 0):
        print("backlog")
    return (skip_count1 == 0 and skip_count2 == 0)
'''    
    
    
    



if __name__ == "__main__":
    string1 = "hello"
    string2 = "hello"
    print("t1: ", backstringCompare(string1, string2))
    
    string3 = "helloo#"
    string4 = "hello"
    print("t2: ", backstringCompare(string3, string4))
    
    string5 = "Uber Career Prep"
    string6 = "u#Uber Careee#r Prep"
    print("t3: ", backstringCompare(string5, string6))
    
    string7 = "abcdef##gh###de"
    string8 = "abc#cde"
    print("t4: ", backstringCompare(string7, string8))
    
    string9 = "#123"
    string10 = "#123"
    print("t5: ", backstringCompare(string9, string10))
    
    string11 = "abcdef"
    string12 = "abcde"
    print("t6: ", backstringCompare(string11, string12))
    
    string13 = "a##"
    string14 = "a##"
    print("t7: ", backstringCompare(string13, string14))
    
    
    
        
        
        