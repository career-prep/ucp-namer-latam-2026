# Technique: forward backward two pointer
# Runtime: O(n)
# Space complexity: O(n)

def ReverseVowels(word):
    left = 0
    right = len(word) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    chars = list(word)
    while left < right:
        leftChar = chars[left]
        while left < right and leftChar not in vowels:
            left +=1
            leftChar = chars[left]

        rightChar = chars[right]
        while left < right and rightChar not in vowels:
            right -=1
            rightChar = chars[right]
        if left < right:
            tmp = chars[left]
            chars[left] = chars[right]
            chars[right] = tmp
        left += 1
        right -=1
    return "".join(chars)




print(ReverseVowels("Uber Career Prep") == "eber Ceraer PrUp")
print(ReverseVowels("xyz") == "xyz")
print(ReverseVowels("flamingo") == "flominga")
print(ReverseVowels("") == "")
print(ReverseVowels("a") == "a")
print(ReverseVowels("aa") == "aa")
print(ReverseVowels("aea") == "aea")
print(ReverseVowels("eaa") == "aae")






# Time spent: 16:30
