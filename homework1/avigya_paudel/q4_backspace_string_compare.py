# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~5 minutes
# TECHNIQUE: Not sure if it aligns with any but reset catchup pointer might work 

def are_same(str1, str2) -> bool:
    """
    Given two strings representing series of keystrokes, 
    are_same determines if the resulting text are same
    backspaces are represented by "#" hence "ab#" = "a"
    @returns bool
    """
    s1_stack, s2_stack = [], []

    for c in str1:
        if c == "#":
            s1_stack.pop()
        else:
            s1_stack.append(c)
    
    for c in str2:
        if c == "#":
            s2_stack.pop()
        else:
            s2_stack.append(c)

    cleaned_s1, cleaned_s2 = "".join(s1_stack), "".join(s2_stack)
    return cleaned_s1 == cleaned_s2

if __name__ == "__main__":
    print(are_same("abcde", "abcde"))                           # Expected: True
    print(are_same("Uber Career Prep", "u#Uber Careee#r Prep")) # Expected: True
    print(are_same("abcdef###xyz", "abcw#xyz"))                 # Expected: True
    print(are_same("abcdef#zyz","abcdefzyz#"))                  # Expected: False