# Data Structure: Stack
# Technique: Push each word onto a stack, pop to build reversed string
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverseWords(s):
    stack = s.split(" ")
    result = []
    while stack:
        result.append(stack.pop())
    return " ".join(result)


# Test 1: "Uber Career Prep" -> "Prep Career Uber"
print(reverseWords("Uber Career Prep"))          # Prep Career Uber

# Test 2: "Emma lives in Brooklyn, New York." -> "York. New Brooklyn, in lives Emma"
print(reverseWords("Emma lives in Brooklyn, New York."))  # York. New Brooklyn, in lives Emma

# Test 3: single word
print(reverseWords("HelloWorld"))                     # HelloWorld

# Test 4: two words
print(reverseWords("Good morning"))              # morning Good

# Test 5: already reversed feel
print(reverseWords("one two three four"))        # four three two one

# Time spent: ~10 minutes