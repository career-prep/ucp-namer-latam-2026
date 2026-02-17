"""
Given a string, reverse the order of the vowels in the string
"""
#Using two pointer techniques, one pointer at the back and one at the front,
#If the front point and back point are vowels, swap them and the shift the pointer
#Else, shift the pointer that is not a vowel.
class solution:
    def ReverseVowels(self, words):
        word = list(words)
        vowels = "aeiouAEIOU"
        left = 0
        right = len(words) - 1
    
        while left < right:
            if word[left] in vowels and word[right] in vowels:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            elif word[left] not in vowels:
                left += 1
            elif word[right] not in vowels:
                right -= 1
        return "".join(word)

sol = solution()   
test_cases = [
    "Uber Career Prep",
    "xyz",
    "flamingo",
    "",
    "a",
    "ab",
    "abc",
    "abcd",
    "hello",
    "HELLO",
    "1234",
    "12 34",
    "!@#$",
    "aa",
    "aaa",
]
for s in test_cases:
    print(sol.ReverseVowels(s))