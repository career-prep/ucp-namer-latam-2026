# Data Structure: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_words(s):
    stack = s.split()
    return " ".join(stack[::-1])

# Time Taken: 2mins 13secs

# Test Cases
print(reverse_words("Uber Career Prep"))
print(reverse_words("Emma lives in Brooklyn New York"))

# Edge Cases
print(reverse_words(""))
print(reverse_words("one"))
print(reverse_words("   hello   world   "))