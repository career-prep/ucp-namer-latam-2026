# Question 7: ReverseWords

# Data Structure: Stack
# Push each word onto a stack, then pop to reverse the order.
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n)


def reverseWords(s):
    stack = s.split(" ")
    result = []
    while stack:
        result.append(stack.pop())
    return " ".join(result)


# --- Tests ---

print(reverseWords("Uber Career Prep"))
# "Prep Career Uber"

print(reverseWords("Emma lives in Brooklyn, New York."))
# "York. New Brooklyn, in lives Emma"

print(reverseWords("hello"))
# "hello"

print(reverseWords("one two"))
# "two one"

print(reverseWords(""))
# ""

# Spent a total of 10 mins on this question
