"""
Given a string, reverse the order of the vowels in the string.

Examples:
Input: "Uber Career Prep" -> Output: "eber Ceraer PrUp"
Input: "xyz" -> Output: "xyz"
Input: "flamingo" -> Output: "flominga"
"""

def reverseVowels_bruteforce(s):
    vowels = set("aeiouAEIOU")
    vowel_list = []
    
    for char in s:
        if char in vowels:
            vowel_list.append(char)
    
    vowel_list.reverse()
    result = []
    idx = 0
    
    for char in s:
        if char in vowels:
            result.append(vowel_list[idx])
            idx += 1
        else:
            result.append(char)
    
    return "".join(result)

# Time Complexity: O(n)
# Space Complexity: O(n)


def reverseVowels_optimal(s):
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    return "".join(s_list)

# Time Complexity: O(n)
# Space Complexity: O(n) for list conversion


test_cases = ["Uber Career Prep", "xyz", "flamingo"]

print("Brute Force:")
for test in test_cases:
    print(reverseVowels_bruteforce(test))

print("\nOptimal:")
for test in test_cases:
    print(reverseVowels_optimal(test))
