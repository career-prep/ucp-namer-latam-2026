# Given a string, return a string that contains only the first occurrence of each character in the string.

# Examples:

# Input String: `"abracadabra"`
# Output: `"abrcd"`

# Input String: `"Uber Career Prep"`
# Output: `"Uber CaPp"`

# Input String: `"zzyzx"`
# Output: `"zyx"`
def FirstOccurence(str):
    res=""
    seen={}
    for i,n in enumerate(str):
        if n in seen:
            continue
        else:
            seen[n]=i
            res+=n
            
    return res
print(FirstOccurence("Uber Career Prep"))
print(FirstOccurence("abracadabra"))
print(FirstOccurence("zzyzx"))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 10 minutes