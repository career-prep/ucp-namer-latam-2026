# two pointer 
# # spent 40 minutes (didnt finish)
# Time complexity - O(n)
# Space complexity - O(n) 

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



def reverseVowels(in_str):
    out_str_left = "" # stores left side of output string
    out_str_right = "" # stores right side of output string 
    
    left = 0
    right = len(in_str)-1
    while left < right:
        if (isVowel(in_str[left]) and isVowel(in_str[right])): # both are vowels --> swap and move
            out_str_left += in_str[right]
            out_str_right = in_str[left] + out_str_right
            right -= 1
            left += 1
            
        elif (isVowel(in_str[left])): # only left is vowel --> move right until vowel found
            out_str_right = in_str[right] + out_str_right
            right -= 1
        
        elif (isVowel(in_str[right])): # only right is vowel --> move left until vowel found
            out_str_left += in_str[left]
            left += 1
            
        else: # no vowels --> add to strings normally and move
            out_str_left += in_str[left]
            out_str_right = in_str[right] + out_str_right
            left += 1
            right -= 1
        
    return out_str_left + out_str_right
                
        
   
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