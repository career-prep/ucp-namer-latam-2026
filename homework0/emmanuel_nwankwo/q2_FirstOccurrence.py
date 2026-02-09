# Time Complexity: O(n)
# Space Complexity: O(n)

def first_occurrence(string):
    s = set()
    output_str = ""

    for char in string:
        if char not in s:
            s.add(char)
            output_str += char

    return output_str

print(first_occurrence("abracadabra"))
print(first_occurrence("Uber Career Prep"))
print(first_occurrence("zzyzx"))

# Time spent: 4mins