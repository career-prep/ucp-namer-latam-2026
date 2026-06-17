#Technique: Forward/backward two pointer method
# reverses the order of the vowels in the input string
def reverseVowels(s:str) -> str:
    vowels = {'a','e','i','o', 'u','A','E','I','O','U'}
    s = list(s) # change to list (strings are immutable)
    l = 0
    r = len(s) - 1

    while l <= r:
        # case 1: s[l] is a vowel, s[r] isn't
        if s[l] in vowels and s[r] not in vowels:
            r -= 1
        # case 2: s[l] isn't a vowel, s[r] is
        elif s[l] not in vowels and s[r] in vowels:
            l += 1
        # case 3: s[l] isn't a vowel, s[r] isn't
        elif s[l] not in vowels and s[r] not in vowels:
            l += 1
            r -= 1
        # case 4: s[l] is a vowel and s[r] is
        else:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1

    return "".join(s)

print("reverseVowels Results:")
test_cases = ["Uber Career Prep",
              "xyz123",
              "flamingo",
              "aeiou",
              "abBA",
              "",
              ]
for test_case in test_cases:
    print(reverseVowels(test_case)) #Expected Output: eber Ceraer PrUp, xyz123, flominga, uoiea, AbBa, ""

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Taken: 21 minutes