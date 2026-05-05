# Data Structure: Stack
# Time Complexity: O(n) since we need to traverse the entire string to split it and then again to join it
# Space Complexity: O(n) since we store the words in a stack and create a new result string

def reverse_words(s):
    words = s.split()

    stack = []
    for word in words:
        stack.append(word)

    reversed_list = []
    while stack:
        reversed_list.append(stack.pop())

    return " ".join(reversed_list)

print(reverse_words("Uber Career Prep"))
print(reverse_words("Emma lives in Brooklyn, New York."))

# Time Spent: 5 min