# Given a string, return a string that contains only the first occurrence of each character in the string.

# Examples:

# Input String: `"abracadabra"`
# Output: `"abrcd"`

# Input String: `"Uber Career Prep"`
# Output: `"Uber CaPp"`

# Input String: `"zzyzx"`
# Output: `"zyx"`
def first_occurence(s):
    res=[]
    seen=set()
    for char in s:
        if char in seen:
            continue
        else:
            seen.add(char)
            res.append(char)
            
    return "".join(res)
print(first_occurence("Uber Career Prep"))
print(first_occurence("abracadabra"))
print(first_occurence("zzyzx"))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 10 minutes