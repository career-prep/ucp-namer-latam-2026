#Time Complexity: 0(n)
#Space Complexity: O(n)
#Technique: stacks

def reverseWords(s):
    stack = []
    
    words = s.split()
    
    for word in words:
        stack.append(word)
        
    result = []
    while stack:
        result.append(stack.pop())
    
    return " ".join(result)

print(reverseWords("Uber Career Prep"))
print(reverseWords("Saad lives in Brooklyn, New York."))

#Time: 20 min