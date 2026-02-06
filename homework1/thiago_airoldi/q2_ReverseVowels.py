# Forward/Backward Two pointer
# O(n) Time complexity where n is the number of chars in the string
# O(n) Space complexity because we needed to convert str to a char array of n chars

str1 = "Uber Career Prep"
str2 = "xyz"
str3 = "flamingo"

def ReverseVowels(str):

    # Convert str to a char array, because string are immutable
    str = list(str)

    def isVowel(c):
        c = c.lower()

        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return True
        else:
            return False



    l = 0
    r = len(str) - 1

    while l < r:

        while l < r and not isVowel(str[l]):
            l += 1

        while l < r and not isVowel(str[r]):
            r -= 1


        # When they both exit, swap
        if l < r:   
            temp = str[l]
            str[l] = str[r]
            str[r] = temp
            # Increment/Decrement l and r so they're no longer on these vowels
            l += 1
            r -= 1

    return "".join(str)

print(ReverseVowels(str1))
print(ReverseVowels(str2))
print(ReverseVowels(str3))


# 19 minutes