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
print(ReverseWords("Rishav loves Sushi."))
print(ReverseWords(""))
print(ReverseWords("yahooo"))
