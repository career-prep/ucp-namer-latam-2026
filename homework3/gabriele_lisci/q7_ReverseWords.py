# Runtime: O(n)
# Space complexity: O(n)
# Data Structure: Stack
# Algorithm: N/A

def ReverseWords(input):
    stack = []
    inputList = input.split(" ")
    for word in inputList:
        stack.append(word)
    res = []
    while stack:
        res.append(stack.pop())
    return " ".join(res)

print(ReverseWords("Uber Career Prep"))
print(ReverseWords("Emma lives in Brooklyn, New York."))
print(ReverseWords(""))
print(ReverseWords("Hey"))

# Note: Couldn't figure out a better way to do this with a different data structure. Wanted to use 2 pointer approach but the data structure would just be a list which is not one of the options.
# Time Spent: 40:00
