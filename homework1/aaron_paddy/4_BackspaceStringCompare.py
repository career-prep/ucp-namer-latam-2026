#Time Complexity: O(N + M) Space Complexity: O(N + M)

def backspace_string_compare(string1, string2):
    def build(str):
        stack = []
        for char in str:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
                
        return "".join(stack)
    
    return build(string1) == build(string2)


def test_cases():
    assert backspace_string_compare('abcde', 'abcde') == True
    assert backspace_string_compare("Uber Career Prep", "u#Uber Careee#r Prep") == True
    assert backspace_string_compare("abcdef###xyz", "abcw#xyz") == True
    assert backspace_string_compare("abcdef###xyz", "abcdefxyz###|") == False
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")


#Time spent: 29 mins
    
    
    
