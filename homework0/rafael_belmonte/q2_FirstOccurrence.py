#Time Complexity: O(n)
#Space Complexity: O(n)
#15 minutes

string1 = "abracadabra"
string2 = "Uber Career Prep"
string3 = "zzyzx"

def first_occurrence(str):
    ocurrences = set() #space O(n)
    new_str = list() #space O(n)
    for i in range(len(str)): #loop time O(n)
        if str[i] not in ocurrences:
            ocurrences.add(str[i]) #add time O(1)
            new_str.append(str[i]) #append time O(1)
    return "".join(new_str) #join time O(n)

#in the worst case, all characters are unique, so space complexity is O(3*n) = O(n)

print(first_occurrence(string1))
print(first_occurrence(string2))
print(first_occurrence(string3))
