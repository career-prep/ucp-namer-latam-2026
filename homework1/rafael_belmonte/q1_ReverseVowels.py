#forward-backward two pointer
#time complexity: O(n)
#space complexity: O(n)
#15 minutes

def reverse_vowels(s):
    vowels = set("aeiouAEIOU") #define vowels
    s = list(s) #convert string to list for mutability
    left, right = 0, len(s) - 1 #initialize pointers, one at the start and one at the end
    while left < right: #loop until pointers meet, then move until they find their respective vowels
        while left < right and s[left] not in vowels: 
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        if left < right: #swap vowels and move pointers inward
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s) #wrap up

#test cases

string1 = "hello"
assert reverse_vowels(string1) == "holle"

string2 = "Uber Career Prep"
assert reverse_vowels(string2) == "eber Ceraer PrUp"

string3 = "xyz"
assert reverse_vowels(string3) == "xyz"

string4 = "flamingo"
assert reverse_vowels(string4) == "flominga"

print("yay!!")