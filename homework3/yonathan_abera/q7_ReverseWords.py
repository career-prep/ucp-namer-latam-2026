# Data Structure: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverseWords(s):
    words = s.split(" ")
    stack = []
    for word in words:
        stack.append(word)

    result = []
    while stack:
        result.append(stack.pop())

    return " ".join(result)


print(reverseWords("Uber Career Prep"))   
print(reverseWords("Emma lives in Brooklyn, New York."))  

# Time spent: 18 minute
