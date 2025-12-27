"""
Given a string, iterate through each character and check wheter it has been seen. 
If it has not been seen, add it to the seen set and append it to the new string.
"""

def FirstOccurrence(str):
    seen = set()
    newstr = ""
    for char in str:
        if char not in seen:
            seen.add(char)
            newstr += (char)

    return newstr

test = ["abracadabra", "Uber Career Prep", "zzyzx"]

for i in test:
    print(FirstOccurrence(i))

# 15 mins