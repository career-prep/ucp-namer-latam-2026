# Question 2: ReverseVowels

# Given a string, reverse the order of the vowels in the string.

# Examples:

# Input String: "Uber Career Prep" # U, e, a, e, e, e -> e, e, e, a, e, U
# Modified String: "eber Ceraer PrUp"

# Input String: "xyz"
# Modified String: "xyz"

# Input String: "flamingo"
# Modified String: "flominga"

# Brute Force Solu
from collections import defaultdict
def ReverseVowels_1(text) -> str:
    vowels = set("aeiouAEIOU")

    vowels_hash = defaultdict(str)
    for i in range(len(text)):
        if text[i] in vowels:
            vowels_hash[i] = text[i]
    
    # before sorting -> {0: 'U', 2: 'e', 6: 'a', 8: 'e', 9: 'e', 14: 'e'}

    # after sorting - > [(14, 'e'), (9, 'e'), (8, 'e'), (6, 'a'), (2, 'e'), (0, 'U')]
    sorted_items = list(reversed(sorted(vowels_hash.values())))

    text = list(text)
    j = 0
    for i in range(len(text)):
        if text[i] in vowels:
            text[i] = sorted_items[j]
            j+=1
    return "".join(text)

# Optimal Solu
def ReverseVowels_2(text) -> str:
    vowels = set("aeiouAEIOU")
    chars = list(text)

    l, r = 0, len(chars) - 1

    while l < r:
        # move left until vowel
        while l < r and chars[l] not in vowels:
            l += 1

        # move right until vowel
        while l < r and chars[r] not in vowels:
            r -= 1

        # swap vowels
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1

    return "".join(chars)

test_cases = ["Uber Career Prep", "xyz", "flamingo"]

print("Brute Force Solu Output")
for test_case in test_cases:
    print(ReverseVowels_1(test_case))

# Time Complexity = O(n)
# Space Complexity = O(n)

print("Optimal Solu Output")
for test_case in test_cases:
    print(ReverseVowels_2(test_case))

# Time Complexity = O(n)
# Space Complexity = O(1) (only list of chars)

# Spent a total of 20 mins on this question