# Time:7 minutes
# Stack
def ReverseWords(word):
    sentence = word.split()
    stack = []
    result = ""
    for word in sentence:
        stack.append(word)
    
    for i in range(len(stack)):
        result += stack.pop() + " "
    return result

print(ReverseWords("Emma lives in Brooklyn, New York."))
print(ReverseWords("Uber Career Prep"))