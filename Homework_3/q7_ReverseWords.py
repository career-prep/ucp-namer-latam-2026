def reverse_words(s):
    stack = []
    temp_word = ""
    for char in s:
        if char == " ":
            if temp_word:
                stack.append(temp_word)
                temp_word = ""
        else:
            temp_word += char
    if temp_word:
        stack.append(temp_word)
    result = ""
    while stack:
        result += stack.pop() + " "
    return result.strip()

print(reverse_words("hello world"))                        
print(reverse_words("one"))                                
print(reverse_words("a b c d e"))                          
print(reverse_words("Go Bears"))                           
print(reverse_words("I love Uber Career Prep"))            
print("Uber Career Prep".split())

#Time Complexity: O(nlogn)
#Space Complexity: O(l) l=length of the word 

#Spent 15 mins