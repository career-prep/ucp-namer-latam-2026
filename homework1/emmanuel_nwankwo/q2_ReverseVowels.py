# Technique: Forward/backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_vowels(s):
    # Return "" for an empty string
    if not s:
        return ""

    s = list(s) # Convert to list
    l = 0
    r = len(s) - 1

    vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}

    while l < r:
        if s[l] in vowels and s[r] in vowels:
            # Found two vowels so swap them
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] in vowels and s[r] not in vowels:
            # Right char isn't a vowel so move right pointer to the left
            r -= 1
        elif s[l] not in vowels and s[r] in vowels:
            # Left char isn't a vowel so move left pointer to the right
            l += 1
        else:
            # Neither side is a vowel move both
            l += 1
            r -= 1

    # Convert back to a string and return
    return "".join(s)

print(reverse_vowels("Uber Career Prep"))
print(reverse_vowels("xyz"))
print(reverse_vowels("flamingo"))

# My Testcases:
print(reverse_vowels("")) # Empty string
print(reverse_vowels("aeiou")) # all vowels
print(reverse_vowels("a")) # single char
print(reverse_vowels("b")) # single non-vowel

# Time Taken: 10mins 38secs