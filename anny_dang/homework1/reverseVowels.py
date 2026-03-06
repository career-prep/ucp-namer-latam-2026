def reverseVowels(s):
    """
    # Technique used: forward/backward two pointer

    # Idea:
    move l forward until it hits a vowel
    move r backward until it hits a vowel 
    swap, then move both inward

    # Complexity:
    Time: O(n)
    Space: O(n)

    # Time spent: 20mins
    """
    n = len(s)
    l, r = 0, n - 1
    s = list(s)

    vowels = {"a", "u", "e", "o", "i", "A", "U", "E", "O", "I"}
    while l < r:
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1

        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    
    return "".join(s)

s1 = "Uber Career Prep"
print(reverseVowels(s1))

s2 = "xyz"
print(reverseVowels(s2))

s3 = "flamingo"
print(reverseVowels(s3))
