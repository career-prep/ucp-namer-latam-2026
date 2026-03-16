'''
    Two pointers & Hashing technique:

    Two pointer left and right
    Move the pointer until both at a vowel
    Swap the elements
    Increment the left and the right until they pass each other

    Time: O(n)
    Space: O(n)
    n: numbers of character inside the string
    
    Time spent: 25 mins
'''

def ReverseVowels(s: str) -> str:
    l, r = 0, len(s) - 1
    # String is immutable so need to convert into a list, O(n) space complexity
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']

    while (l < r):
        # Find the vowels to swap
        while s[l].lower() not in vowels and l < r:
            l += 1
        while s[r].lower() not in vowels and l < r:
            r -= 1
        # Swap the vowels
        s[l], s[r] = s[r], s[l]
        # Increment the pointers
        l += 1
        r -= 1

    return "".join(s)

s = "Uber Career Prep"
print(ReverseVowels(s))
s = "xyz"
print(ReverseVowels(s))
s = "flamingo"
print(ReverseVowels(s))