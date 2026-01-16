#given a STRING
# return a STRING with frist occurance of each char in the string

def firstOccur(stng):
    new_str = ""
    for char in stng:
        if char not in new_str:
            new_str += char
    return new_str

print(firstOccur("abracadabra"))
print(firstOccur("Uber Career Prep"))
print(firstOccur("zzyzx"))