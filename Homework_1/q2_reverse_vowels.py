# Question 2: ReverseVowels

# Given a string, reverse the order of the vowels in the string.

# Examples:

# Input String: "Uber Career Prep"
# Modified String: "eber Ceraer PrUp"

# Input String: "xyz"
# Modified String: "xyz"

# Input String: "flamingo"
# Modified String: "flominga"
def reverse_vowels(strings):
    new = list(strings)
    vowels = "aeiouAEIOU"
    l,r=0,len(strings)-1
    while l<r:
        while l<r and new[l] not in vowels:
            l+=1
        while l<r and new[r] not in vowels:
            r-=1
        new[l],new[r]=new[r],new[l]
        l+=1
        r-=1
    return "".join(new)



print(reverse_vowels("hello"))      
print(reverse_vowels("leetcode"))   
print(reverse_vowels("aA"))      
print(reverse_vowels("flamingo"))


#Time Complexity: O(n)
#Space Complexity: O(n)
#Spent 20 mins