"""
Technique: Reset/catch up 2 pointers
Time Complexity: O(n+m)
Space Complexity: O(n+m)
n is length of s1
m is length of s2
"""


"""
Problem:
2 strings represent series of key strokes: s1, s2
return True if resulting text is the same; otherwise false

Backspace is: #
=> "x#" = ""   

#ideas:
we gonna use 2 ptr, 1 for the 1st string and another for the 2nd string
since # means delete, but to moving back for a pointer is hard=> we gonna place the pointers to run from the end of the array so that whenever it meet #, it will skip the correspond number of element

i was thinking of decoding each variable and then compare it together
=> def decode_srting(s):
create an array as a placeholder for the char
looping through the string, if char ="#" => track the number of "#" so that we can skip later on
if there is no # left => add the elem to the array

finally, compare the 2 array
"""

def backspace_string_compare(s1,s2):
    return decode_string(s1)== decode_string(s2)

def decode_string(s):
    skip=0
    arr=[]
    for i in range(len(s)-1,-1,-1):
        if s[i]=="#":
            skip+=1
            continue

        if skip>0:
            skip-=1
            continue

        arr.append(s[i])
    return arr

print(backspace_string_compare("abcde","abcde"))
print(backspace_string_compare("Uber Career Prep","u#Uber Careee#r Prep"))
print(backspace_string_compare("abcdef###xyz", "abcw#xyz"))
print(backspace_string_compare("abcdef###xyz", "abcdefxyz###"))



    



    
        


    