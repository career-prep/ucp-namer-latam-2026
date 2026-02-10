#two arrays/strings two-pointer
#time complexity: O(n+m) 
#space complexity:  O(1)
#36 minutes

def backspace_string_compare(s, t):
    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0: #while there are characters to process
        erase_s = 0
        while i >= 0: #process backspaces in s
            if s[i] == '#':
                erase_s += 1
                i -= 1
            elif erase_s > 0:
                erase_s -= 1
                i -= 1
            else:
                break
        erase_t = 0
        while j >= 0: #process backspaces in t
            if t[j] == '#':
                erase_t += 1
                j -= 1
            elif erase_t > 0:
                erase_t -= 1
                j -= 1
            else:
                break
        if i >= 0 and j >= 0: #both strings have characters left
            if s[i] != t[j]: 
                return False
        elif i >= 0 or j >= 0: #one string has characters left
            return False
        i -= 1
        j -= 1
    return True

#test cases

string1_1 = "abcde"
string1_2 = "abcde"
assert backspace_string_compare(string1_1, string1_2) == True

string2_1 = "Uber Career Prep"
string2_2 = "u#Uber Careee#r Prep"
assert backspace_string_compare(string2_1, string2_2) == True

string3_1 = "abcdef###xyz"
string3_2 = "abcw#xyz"
assert backspace_string_compare(string3_1, string3_2) == True

string4_1 = "abcdef###xyz"
string4_2 = "abcdefxyz###"
assert backspace_string_compare(string4_1, string4_2) == False

print("yohooo!")