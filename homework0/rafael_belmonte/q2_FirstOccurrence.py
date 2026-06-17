#Time Complexity: O(n)
#Space Complexity: O(n)
#15 minutes

string1 = "abracadabra"
string2 = "Uber Career Prep"
string3 = "zzyzx"

def first_occurrence(s):
    ocurrences = set() #space O(n)
    new_s = list() #space O(n)
    for char in s: #loop time O(n)
        if char not in ocurrences:
            ocurrences.add(char) #add time O(1)
            new_s.append(char) #append time O(1)
    return "".join(new_s) #join time O(n)

#in the worst case, all characters are unique, so space complexity is O(3*n) = O(n)

print(first_occurrence(string1))
print(first_occurrence(string2))
print(first_occurrence(string3))
