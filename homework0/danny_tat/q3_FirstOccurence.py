"""
Given a string, return a string that contains only the first occurrence 
of each character in the string.

Examples:
Input String: "abracadabra"
Output: "abrcd"

Input String: "Uber Career Prep"
Output: "Uber CaPp"

Input String: "zzyzx"
Output: "zyx"
"""


def first_occurence(word):
    my_map = {}
    result = ""

    for char in word:
        my_map[char] = my_map.get(char, 0) + 1

        if my_map[char] == 1:
            result += char

    return result


print(first_occurence("abracadabra"))
print(first_occurence("Uber Career Prep"))
print(first_occurence("zzyzx"))
