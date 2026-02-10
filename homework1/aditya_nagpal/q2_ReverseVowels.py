#p1
## time taken: 18mins
## time complexity: 0(n)
## method used: two pointers

#p2
    ##given: a string
    ## return: the reverse order of the vowels

#solution

def ReverseVowels(strn):

    i = 0
    j = len(strn) -1
    strn = list(strn) 

    arr = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    while(i <j):
        if strn[i] in arr:
            if strn[j] in arr:
                strn[i], strn[j] = strn[j], strn[i]
                i = i+ 1
                j = j-1
            else:
                j = j -1 
        else:
            i = i+1

    return "".join(strn)


print(ReverseVowels("Uber Career Prep"))
print(ReverseVowels("xyz"))
print(ReverseVowels("flamingo"))
