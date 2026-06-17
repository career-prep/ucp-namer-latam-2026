# Question 2: ReverseVowels

# Given a string, reverse the order of the vowels in the string.

# Examples:

# Input String: "Uber Career Prep"
# Modified String: "eber Ceraer PrUp"

# Input String: "xyz"
# Modified String: "xyz"

# Input String: "flamingo"
# Modified String: "flominga"
def reverse_vowels(s):
    chars = list(s)
    vowels = "aeiouAEIOU"
    l,r=0,len(s)-1
    while l<r:
        while l<r and chars[l] not in vowels:
            l+=1
        while l<r and chars[r] not in vowels:
            r-=1
        chars[l],chars[r]=chars[r],chars[l]
        l+=1
        r-=1
    return "".join(chars)



print(reverse_vowels("hello"))      
print(reverse_vowels("leetcode"))   
print(reverse_vowels("aA"))      
print(reverse_vowels("flamingo"))


#Time Complexity: O(n)
#Space Complexity: O(n)
#Spent 20 mins