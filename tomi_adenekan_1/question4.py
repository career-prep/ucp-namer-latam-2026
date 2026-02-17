"""
40 minutes
time complexity = O(n)
space complexity = O(n)
"""

def check(str):
    stack = []
    for i in range(len(str)):
        if str[i] != "#":
            stack.append(str[i])
        elif str[i] == "#" and len(stack) >0:
            stack.pop()
        else:
            continue

    return "".join(stack)

def get_name(str1, str2):
    check1 = check(str1)
    check2 = check(str2)

    return check1 == check2





str1 = "abcdef###xyz"
str2 = "abcw#xyz"

print(get_name(str1, str2))
    
    
