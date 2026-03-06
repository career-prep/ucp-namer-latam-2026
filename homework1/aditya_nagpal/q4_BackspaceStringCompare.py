#this question took longer to understand
#given:
    ## two string
    ## every hash pressed("#") represents a back stroke

# what to do:
    ## check whether the two string are equal or not

# implementation:

#def stringCheck(str1, str2):
#   l1 = list(str1)
#   n = len(l1)
#  
#   j = 0
#   while(j < n):
#       if(l1[j] == "#"):
#           l1.pop(j-1)
#           l1.pop(j)
#       j = j+1

#   l2 = list(str2)
#   n2 = len(l2)
#   j2 = 0
#   while(j2 < n2):
#       if(l2[j2] == "#"):
#           l2.pop(j2-1)
#           l2.pop(j2)
#       j2 = j2+1

#   if l1 == l2:
#       return true

#   return false   # the problem faced is the original list get manuplated

# time taken: 25 mins
# logic used : stacks
# space and time: O(m+n)

def stringCheck(str1, str2):
    stack = []

    for ch in str1:
        if ch != "#":
            stack.append(ch)
        elif stack:
            stack.pop()


    stack2 = []

    for ch2 in str2:
        if ch2 != "#":
            stack2.append(ch2)
        elif stack2:
            stack2.pop()

    if stack == stack2:
        return True
    
    return False
        
