# two pointer 
# # spent 40 minutes (didnt finish)
# Time complexity - O(n)
# Space complexity - O(n) 

# checks if a character is a vowel
def isVowel(c):
    return (c.lower() in "aeiou")
    



def reverseVowels(in_str):
    in_str_list = list(in_str) # convert to list to allow for mutation
    left = 0 
    right = len(in_str)-1
    while left < right:
        char_left = in_str_list[left]
        char_right = in_str_list[right]
        
        if (isVowel(char_left) and isVowel(char_right)): # both are vowels -> swap and move
            in_str_list[left], in_str_list[right] = char_right, char_left
            left += 1
            right -= 1
        elif (isVowel(char_left)): # only left is vowel -> move right until vowel found
            right -= 1
        elif (isVowel(char_right)): # only right is vowel -> move left until vowel found
            left += 1
        else: # no vowels -> move both pointers
            left += 1
            right -= 1
            
    out_str = "".join(in_str_list) # convert back to string
    return out_str



   
if __name__ == "__main__":
    str1 = "Uber Career prep"
    out1 = reverseVowels(str1)
    print("test1:", out1)
    
    str2 = "xyz"
    out2 = reverseVowels(str2)
    print("test2: ", out2)
    
    str3 = "flamingo"
    out3 = reverseVowels(str3)
    print("test3: ", out3)
    


# forgot strings are immutable in py
'''
# checks if a character is a vowel
def isVowel(c):
    ascii_c = ord(c) # ascii
    # check uppercase
    if (ascii_c == 65 or ascii_c == 69 or ascii_c == 73 or ascii_c == 79 or ascii_c == 85):
        return True
    # check lowercase
    ascii_c -= 32
    if (ascii_c == 65 or ascii_c == 69 or ascii_c == 73 or ascii_c == 79 or ascii_c == 85):
        return True
    return False



def reverseVowels(string):
    left = 0
    right = len(string)-1
    while left < right:
        if isVowel(string[left]): # left stores vowel
            if isVowel(string[right]): # both store vowel
                # swap
                temp = string[left]
                string[left] = string[right]
                string[right] = temp
                # update
                left += 1
                right -= 1
            else: # move right pointer until find vowel
                right -= 1
                
        elif isVowel(string[right]): # right stores vowel
            if isVowel(string[left]): # both store vowel
                # swap
                temp = string[left]
                string[left] = string[right]
                string[right] = temp
                # update
                left += 1
                right -= 1
            else: # move left pointer until vowel
                left += 1
                
        else: # neither vowels
            left += 1
            right -= 1
            
    return string
                
    
    
if __name__ == "__main__":
    str1 = "Uber Career prep"
    out1 = reverseVowels(str1)
    print("test1:", out1)
    
    str2 = "xyz"
    out2 = reverseVowels(str2)
    print("test2: ", out2)
    
    str3 = "flamingo"
    out3 = reverseVowels(str3)
    print("test3: ", out3)
'''