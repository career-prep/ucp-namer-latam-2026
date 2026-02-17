"""
Technique: Forward/backward 2 pointers
Time Complexity: O(n) 
Space Complexity: O(n)
"""

"""
Problems:
given a string: str
reverse the order of vowels in string

capitalization does matter
we can only reverse, not making a new string

Examples
str= "Uber Career Prep"
output: "eber Ceraer PrUp" 

explain: the vowels are: u,e,o,a,i
order of vowel in strs: U,e,a,e,e,e
=> reverse: e,e,e,a,e,U

Example:
str = "flamingo"
output: flominga

APPROACH:
We wanna reverse the order => we can swap the correspond pair of vowel (swapping from vowel from the start to the end)
for example 1: we gonna swap: U->e, e->e, a->e
we wanna find the vowel from the start and the end of the string at the same time in order to swap it 
=> We gonna use Forward/Backward 2 pointers

we gonna create a set that store the vowel so that we can check if the char is a vowel or not with a const time
since the string is immutable => we cannot swap the char => we could change it into a list and swap the char

next, we gonna create 2 ptr: l=0, r=len(str)-1 to find the vowel from forward and backward
there is gonna be 2 main cases:

CASE 1:
while left or right ptr is not at vowel => move them

CASE 2:
they are both at the vowel => swap them

after all the steps, we gonna convert the arr back into a string

"""

#helper
def vowel_check(c):
    vowels={"u","e","o","a","i"}
    if c.lower() in vowels:
        return True
    return False

#function
def reverse_vowels(str):
    arr=[]
    for char in str:
        arr.append(char)

    l=0
    r=len(arr)-1

    while l<r:
        
        while l<r and vowel_check(arr[l])==False:
            l+=1
        
        while l<r and vowel_check(arr[r])==False:
            r-=1
        
        temp=arr[r]
        arr[r]=arr[l]
        arr[l]=temp
        l+=1
        r-=1
    
    return "".join(arr)



print(reverse_vowels("Uber Career Prep"))
print(reverse_vowels("flamingo"))


        





        

        