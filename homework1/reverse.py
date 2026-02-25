# Question 2: Reverse Vowels
# Given a string, reverse the order of the vowels in the string.
# Examples:
# Input String: "Uber Career Prep"
# Modified String: "eber Ceraer PrUp"
# Input String: "xyz"|
# Modified String: "xyz"
# Input String: "flamingo"
# Modified String: "flominga"


# Technique- 2 pointers technique- forward and backward 
# time- 40 mins
# time complexity- each pointer moves in only one direction so it is o(N) 

def reverse_vowels(s):
    list_str = list(s)
    vowels = set("aeiouAEIOU")
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and list_str[l] not in vowels:
            l += 1
        while l < r and list_str[r] not in vowels:
            r -= 1

        list_str[l], list_str[r] = list_str[r], list_str[l]
        l += 1
        r -= 1

    return "".join(list_str)

print(reverse_vowels("Uber Career Prep")) #"eber Ceraer PrUp"
print(reverse_vowels("xyz")) #"xyz"
print(reverse_vowels("flominga")) #"flominga"