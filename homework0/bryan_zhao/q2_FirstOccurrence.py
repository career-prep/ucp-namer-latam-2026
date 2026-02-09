#Time Complexity: O(n)
#Space Complexity: O(n)

def first_occurrence(s: str) -> str:
    unique_letters = set()
    unique_str = ""

    for char in s:
        if char not in unique_letters:
            unique_letters.add(char)
            unique_str += char
    
    return unique_str

string1 = "abracadabra"
#Output: "abrcd"

string2 = "Uber Career Prep"
#Output: "Uber CaPp"

string3 = "zzyzx"
#Output: "zyx"

print(first_occurrence(string1))
print(first_occurrence(string2))
print(first_occurrence(string3))

#Time spent on first_occurrence: 9 minutes