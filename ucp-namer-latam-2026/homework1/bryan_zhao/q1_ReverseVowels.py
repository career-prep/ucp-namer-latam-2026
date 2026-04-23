"""
Technique Used: Forward/backward two-pointer
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Input: input string
# Output: modified string with vowels reversed
# Approach: Since the input strings allow for both uppercase and lowercase letters, store
# all possible vowels in a set to quickly check if the character we are on is a vowel or not.
# Set left pointer to start of string and right pointer at the end. Check each individual letter
# and see if they are a vowel. If so, do not shift the pointer and stay there until the other
# pointer finds a vowel. Swap the vowels after both pointers have found a vowel and repeat until
# pointers converge.
# Potential Edge Cases: No vowels in the string, empty string, odd number of vowels (?)

def reverse_vowels(s: str) -> str:
    if not s:
        return ""
    
    left, right = 0, len(s) - 1
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)

    while left < right:
        if s[left] in vowel_set and s[right] in vowel_set:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowel_set:
            left += 1
        else:
            right -= 1   
    
    return "".join(s)

print(reverse_vowels("Uber Career Prep"))
print(reverse_vowels("xyz"))
print(reverse_vowels("flamingo"))

#Time Spent: 10 minutes