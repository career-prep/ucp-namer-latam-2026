def ReverseVowels(string):

    '''
    Forward / backward two pointer
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    vowels = "aeiouAEIOU"
    string= list(string)

    left = 0
    right= len(string) - 1
    
    while left < right:
        
        left_is_vowel = string[left] in vowels
        right_is_vowel = string[right] in vowels

        if left_is_vowel and right_is_vowel:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        else:
            if not left_is_vowel:
                left += 1
            if not right_is_vowel:
                right -= 1
                
    return "".join(string)

# Time taken: 20mins

# string = "Uber Career Prep"
# output = "eber Ceraer PrUp"

# string = "flamingo"
# output = "flominga"

# print(ReverseVowels(string))   

