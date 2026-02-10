"""
Time, Space complexities: O(n), O(1)
q4: BackspaceStringCompare

Given two strings representing series of keystrokes, determine wheter the resulting 
text is the same. Backspaces are represented by the '#' character so "x#" results in the
empty string ("").
"""

def backSpaceStringCompare(s1, s2):
    #1. Initialize pointers at the end of each string
    p1 = len(s1) - 1
    p2 = len(s2) - 1

    while p1 >= 0 or p2 >= 0:
        #2. Find the next valid character in s1
        p1 = get_next_valid_char_index(s1, p1)
        #3. Find the next valid character in s2
        p2 = get_next_valid_char_index(s2, p2)

        #4. If both are valid indices, compare the characters
        if p1 >= 0 and p2 >= 0:
            if s1[p1] != s2[p2]:
                return False
        #5. If one string is exhausted but the other isn't, they aren't equal
        elif p1 >= 0 or p2 >= 0:
            return False

        p1 -= 1
        p2 -= 1

    return True

def get_next_valid_char_index(string, index):
    # Helper to skip characters affected by backspaces
    backspace_count = 0
    while index >= 0:
        if string[index] == '#':
            backspace_count += 1
            index -= 1
        elif backspace_count > 0:
            backspace_count -= 1
            index -= 1
        else:
            break
    return index


def test_BSC():
    input_strings = ("abcde", "abcde")
    expected = True
    result = backSpaceStringCompare(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("Uber Career Prep", "u#Uber Careee#r Prep")
    expected = True
    result = backSpaceStringCompare(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("abcdef###xyz", "abcw#xyz")
    expected = True
    result = backSpaceStringCompare(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("abcdef###xyz", "abcdefxyz###")
    expected = False
    result = backSpaceStringCompare(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_BSC()