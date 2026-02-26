# Question 2 (Reverse Vowels)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 23 mins

def reverseVowels(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    vowels = set('aeiouAEIOU')

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1

        while left < right and s[right] not in vowels:
            right -= 1

        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)




#Tests
print(reverseVowels("Uber Career Prep"))  # eber CarUer Prep
print(reverseVowels("hello"))             # holle
print(reverseVowels("leetcode"))          # leotcede
print(reverseVowels("aA"))                # Aa
print(reverseVowels("bcdfg"))              # bcdfg
