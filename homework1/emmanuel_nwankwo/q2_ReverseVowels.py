# Technique: Forward/backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_vowels(s):
    if not s:
        return ""
    s = list(s)
    l = 0
    r = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}

    while l < r:
        if s[l] in vowels and s[r] in vowels:
            temp_l = s[l]
            temp_r = s[r]
            s[l], s[r] = temp_r, temp_l
            l += 1
            r -= 1
        elif s[l] in vowels and s[r] not in vowels:
            r -= 1
        elif s[l] not in vowels and s[r] in vowels:
            l += 1
        else:
            l += 1
            r -= 1

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