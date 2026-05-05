# Data Structure: Stack
# Algorithm: Stack Push / Pop
# Time Complexity: O(n)
# Space Complexity: O(n)
# Problem: Given a string, return the string with the order of the
#          space-separated words reversed.

def reverseWords(s):
    stack = []
    for word in s.split(" "):
        stack.append(word)
    result = []
    while stack:
        result.append(stack.pop())
    return " ".join(result)


# Testing:
print(reverseWords("Uber Career Prep"))  # "Prep Career Uber"
# "York. New Brooklyn, in lives Emma"
print(reverseWords("Emma lives in Brooklyn, New York."))

# Time: 10 min
