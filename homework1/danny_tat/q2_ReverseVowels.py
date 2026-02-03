# time: O(n)
# space: O(n)

"""
Given a string, reverse the order of the vowels in the string
EX: 
input string = "Uber Career Prep"
modified string = "eber Ceraer PrUp"

input string: "xyz"
modified string : "xyz"

input string: "flamingo"
modified string : "flominga"
"""


def swap_vowel(str):
    n = len(str)
    l = 0
    r = n - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = list(str)

    while l <= r:
        if str[l].lower() not in vowels:
            l += 1
        elif str[r].lower() not in vowels:
            r -= 1
        else:
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1
    return "".join(result)


print(swap_vowel("Uber Career Prep"))
print(swap_vowel("xyz"))
print(swap_vowel("flamingo"))
print(swap_vowel("AEIOU"))
print(swap_vowel(""))
print(swap_vowel("AFKeaneAE"))


# 19 minutes
