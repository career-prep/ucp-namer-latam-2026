# Time complexity: O(n)
# Space complexity: O(n); because strings are immutable in Python, we have to convert to list

# Technique: Forward/backward two-pointer

def ReverseVowels(str):
    left, right, s = 0, len(str)-1, list(str)

    vowels = {'a', 'e', 'i', 'o', 'u'}

    while left < right:
        while s[left].lower() not in vowels:
            left += 1
        while s[right].lower() not in vowels:
            right -= 1
        
        if left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

    return "".join(s)
        
if __name__ == '__main__':
    # inputStr = "Uber Career Prep"
    # inputStr = "xyz"
    # inputStr = "flamingo"
    inputStr = "oiae"
    print("Input String:", inputStr)
    print("Output:", ReverseVowels(inputStr))

# ~ time spent: 18 minutes