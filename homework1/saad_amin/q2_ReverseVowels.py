#Technique : Forward/ backward two pointer
#Time Complexity O(n)
#Space Complexity O(n) due to list


def reverseVowels(s):
    if not s:
        return ""
    
    strr = list(s)
    
    vowels = set("AEIOUaeiou")
    
    l = 0
    r = len(strr) - 1

    while l < r:
        while l < r and strr[l] not in vowels:
            l += 1

        while l< r and  strr[r] not in vowels:
            r -= 1

        strr[l], strr[r] = strr[r], strr[l]
        l += 1
        r -= 1

    return "".join(strr)

print(reverseVowels("Uber Career Prep"))
print(reverseVowels("flamingo"))
print(reverseVowels("Saad Amin"))

#Time taken : 22 min

        
