#Forward Backward Two Pointer
#O(n) time, O(n) space
#Assumptions: 
#String is non-empty
def reverse_vowels(characters):
    vowels = {"a", "e", "i", "o", "u"}
    l, r = 0, len(characters) - 1
    acc = list(characters)

    while l < r:
        if (acc[l]).lower() in vowels and (acc[r]).lower() in vowels:
            acc[l], acc[r] = acc[r], acc[l]
            l+=1
            r-=1
        elif (acc[l]).lower() in vowels:
            r -= 1
        else:
            l += 1
    final = "".join(acc)
    return final

print(reverse_vowels("Uber Career Prep"))
print(reverse_vowels("Flamingo"))
print(reverse_vowels("leetcode"))
print(reverse_vowels("hello world"))
print(reverse_vowels("AEIOU"))
print(reverse_vowels("Python"))
print(reverse_vowels("aA"))

#15 minutes
