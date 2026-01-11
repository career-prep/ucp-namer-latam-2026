#Time Complexity: O(n)
#Space Complexity: O(n)

string1 = "abracadabra"
string2 = "Uber Career Prep"
string3 = "zzyzx"

def first_occurrence(str):
    ocurrences = set()
    new_str = list()
    for i in range(len(str)):
        if str[i] not in ocurrences:
            ocurrences.add(str[i])
            new_str.append(str[i])
    return "".join(new_str)

print(first_occurrence(string1))
print(first_occurrence(string2))
print(first_occurrence(string3))

#15 minutes