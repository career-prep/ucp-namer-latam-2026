"""
Technique Used: Forward Backward Two Pointer
Time Complexity: O(log n)
Space Complexity: O(n)

Intuition: Rewrite the string into a list. 
Use the forward backward two pointer technique to find vowels from the front and back of the array.
When both pointers find a vowel, swap them. Continue until the pointers meet in the middle.
"""
def ReverseVowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)

    front = 0
    back = len(s) - 1

    while front < back:
        if s[front] not in vowels:
            front += 1
        elif s[back] not in vowels:
            back -= 1
        else:
            temp = s[front]
            s[front] = s[back]
            s[back] = temp
            front += 1
            back -= 1
    return "".join(s)

# Test Cases
test = ["Uber Career Prep",
        "xyz",
        "flamingo",
        "",
        "aA"]

for i in test:
    print(ReverseVowels(i))

# Time Spent: 20 mins