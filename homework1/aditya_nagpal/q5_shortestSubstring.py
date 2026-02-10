#givem:
## two string

# find or solve for:
## return the length of the shortest substring in 1st string containing all the ch in the 2nd string

# solution:
def shortestSubString(firstStr, secondStr):

    i = j = 0
    newStr = ""
    while( i < len(firstStr) and j < len(secondStr)):
            if firstStr[i] != secondStr[j]:
                i = i +1
            else:
                newStr += secondStr[j]
        
                j = j + 1
                i = i + 1

    return newStr

print(shortestSubString("abracadabra", "abc"))
print(shortestSubString("dog", "god"))


