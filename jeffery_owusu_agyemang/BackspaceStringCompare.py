# Question 4 (Backspace String Compare)
#  Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 10 mins



def backspaceCompare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return process_string(s) == process_string(t)



# Q4
print(backspaceCompare("ab#c", "ad#c"))     # True
print(backspaceCompare("ab##", "c#d#"))     # True
print(backspaceCompare("a#c", "b"))         # False
print(backspaceCompare("###", ""))          # True
