# Question 3: First Occurrence
# Given a string => return a string that contains the first occurrence of each char

# Approach:
# create a set that stores the unique elements
# if elem not in the set, add to the string and add them in the set

# => Spend 5 mins

# Implementation:

def first_occurance(s):
    returned_str=""
    unique_char=set()

    for char in s:
        if char not in unique_char:
            returned_str+=char
            unique_char.add(char)
            
    return returned_str

# test case:
print(first_occurance("abracadabra"))
print(first_occurance("Uber Career Prep"))
print(first_occurance("zzyzx"))


 
