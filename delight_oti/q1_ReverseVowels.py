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
        
        if string[left] in vowels and string[right] in vowels:
            temp= string[right]
            string[right] = string[left]
            string[left] = temp
            
            left+=1
            right-=1
        else:
            if string[left] not in vowels:
                left+=1

            if string[right] not in vowels:
                right-=1
                
    return "".join(string)

# Time taken: 20mins

# string = "Uber Career Prep"
# output = "eber Ceraer PrUp"

# string = "flamingo"
# output = "flominga"

# print(ReverseVowels(string))   

