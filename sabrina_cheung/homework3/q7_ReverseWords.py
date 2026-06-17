# Method: Stack
# Space Complexity: O(N)
# Time Complexity: O(N)
# Total Time Taken: 15 mins

def ReverseWords(str):
    if str is None:
        return ""
    
    word = ""
    stack = []
    for char in str:
        if char == " ":
            if word:
                stack.append(word)
                word = ""
        else:
            word += char
    if word:
        stack.append(word)

    reversed = ""
    while stack:
        reversed += stack.pop()
        if stack:
            reversed += " "
    return reversed

print(ReverseWords("Uber Career Prep"))
print(ReverseWords("Emma lives in Brooklyn, New York."))
print(ReverseWords("Hello  World"))