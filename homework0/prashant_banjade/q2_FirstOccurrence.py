# Question 3: firstoccurence
# Given a string, return a string that contains only the first occurrence of each character in the string.
# Examples:
# Input String: "abracadabra".   Output: "abred"
# input String: "Uber Career Prep".   Output: "Uber CaPp"
# Input String: "zzyzx".   Output: "zyx"

def firstoccurrence(st):
    seen= set()
    res=[]
    for ch in st:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)

print(firstoccurrence("abracadabra"))
print(firstoccurrence("Uber Career Prep"))
print(firstoccurrence("zzyzx"))



