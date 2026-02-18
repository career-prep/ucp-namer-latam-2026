#Samaksh Arora
#BackspaceStringCompare
#Time Complexity: O(n + m)
#Space Complexity: O(n + m)
#Stacks
def BackSpaceStringCompare(string1, string2):
    stack1 = []
    stack2 = []

    for letter in string1:
        if letter == "#" and stack1:
            stack1.pop()

        elif letter != "#":
            stack1.append(letter)
    
    for letter in string2:
        if letter == "#" and stack2:
            stack2.pop()
        elif letter != "#":
            stack2.append(letter)
    
    return stack1 == stack2
        

string1 = "abcdef###xyz"
string2 = "abcw#xyz"
print(BackSpaceStringCompare(string1, string2)) #output= True

string1 = "abcdef###xyz"
string2 = "abcdxyz###"
print(BackSpaceStringCompare(string1, string2)) #output = False

#Time Spent: 25 minutes
    
        


    