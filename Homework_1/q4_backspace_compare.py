# Given two strings representing series of keystrokes, determine whether the 
# resulting text is the same. Backspaces are represented by the '#' character 
# so "x#" results in the empty string ("").

# Examples:

# Input Strings: "abcde", "abcde"
# Output: True

# Input Strings: "Uber Career Prep", "u#Uber Caree#r Prep"
# Output: True

# Input Strings: "abcdef###xyz", "abcw#xyz"
# Output: True

# Input Strings: "abcdef###xyz", "abcdefxyz###"
# Output: False

def backspace_compare(string1,string2):
    def remove_hash(s):
        stack=[]
        for c in s:
            if c!="#":
                stack.append(c)
            elif stack:
                stack.pop()
        return ''.join(stack)


    return remove_hash(string1)==remove_hash(string2)

print(backspace_compare("abcdef###xyz", "abcdefxyz###"))
print(backspace_compare("ab#c", "ac"))
print(backspace_compare("bxj##tw", "bxo#j##tw"))
print(backspace_compare("abc####", ""))
print(backspace_compare("y#fo##f", "y#f#o##f"))
print(backspace_compare("hello", "world"))

#Time Complexity: O(n+m)
#Space Complexity: O(n+m)
#Spent 12 mins