# Question 3: First Occurrence
# Given a string => return a string that contains the first occurrence of each char

# Approach:
# create a set that stores the unique elements
# if elem not in the set, add to the string and add them in the set

# => Spend 5 mins

# Implementation:

def first_occurance(s):
    res=""
    unique_char=set()

    for c in s:
        if c not in unique_char:
            res+=c
            unique_char.add(c)
            
    return res

# test case:
print(first_occurance("abracadabra"))
print(first_occurance("Uber Career Prep"))
print(first_occurance("zzyzx"))


 
