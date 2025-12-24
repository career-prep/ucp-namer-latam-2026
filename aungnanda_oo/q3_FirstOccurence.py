# Given a string, return a string that contains only the first occurrence of each character in the string.

# Examples:

# Input String: "abracadabra"
# Output: "abrcd"

# Input String: "Uber Career Prep"
# Output: "Uber CaPp"

# Input String: "zzyzx"
# Output: "zyx"



def FirstOccurrence(string_input):
    seen = set()
    res = ''
    for letter in string_input:
        if letter not in seen:
            seen.add(letter)
            res += letter
    return res


# O(n) time, O(n) space
test_list = ["abracadabra","Uber Career Prep","zzyzx"]
for test in test_list:
    print(FirstOccurrence(test))

# Spent a total of 7 mins on this question