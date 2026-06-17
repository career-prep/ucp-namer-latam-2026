"""
Technique Used: Forward/backward two-pointer
Time Complexity: O(n + m), n = length of str1, m = length of str2
Space Complexity: O(1)
"""

# Input: two strings, str1 and str2 representing series of keystrokes
# Output: true/false statement determining if the two strings are the same
# Approach: Instead of moving from front to back, work from back to front so that I can be
# certain that the letters that follow the "#" will be characters I skip. Set right pointers
# for both strings, then keep track of how many "#" I find to determine how many times I need
# to skip letters. Compare the next valid character in each string and see if they are equal.
# If not, immediately return False and terminate the code because it is impossible for them to
# be equal anymore.
# Edge Cases: Both empty strings, one empty and one not

def backspace_string_compare(str1: str, str2: str) -> bool:
    right_ptr1, right_ptr2 = len(str1) - 1, len(str2) - 1

    while right_ptr1 >= 0 or right_ptr2 >= 0:
        right_ptr1 = get_next_index(str1, right_ptr1)
        right_ptr2 = get_next_index(str2, right_ptr2)

        if right_ptr1 >= 0 and right_ptr2 >= 0:
            if str1[right_ptr1] != str2[right_ptr2]:
                return False
        elif (right_ptr1 >= 0) != (right_ptr2 >= 0):
            return False
        
        right_ptr1 -= 1
        right_ptr2 -= 1

    return True

def get_next_index(string: str, index: int) -> int:
    skip = 0
    while index >= 0:
        if string[index] == '#':
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            break # If we haven't found a '#' and we're out of skips, this is our valid index
        index -= 1
    
    return index

print(backspace_string_compare("abcde","abcde"))
print(backspace_string_compare("Uber Career Prep","u#Uber Careee#r Prep"))
print(backspace_string_compare("abcdef###xyz", "abcw#xyz"))
print(backspace_string_compare("abcdef###xyz", "abcdefxyz###"))
print(backspace_string_compare("", "")) # Added test case to test for empty strings
print(backspace_string_compare("abc#de", "")) # Added test case to test for an empty and non-empty string

# Time Spent: 40 minutes