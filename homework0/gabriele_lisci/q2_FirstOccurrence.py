#Time Complexity: O(n)
#Space Complexity: O(n)

def FirstOccurence(input):
    seen = {}
    result = ""
    for c in input:
        if c not in seen:
            result += c
            seen[c] = 1
    return result

print(FirstOccurence("abracadabra") == "abrcd")
print(FirstOccurence("Uber Career Prep") == "Uber CaPp")
print(FirstOccurence("zzyzx") == "zyx")

#Spent 3 minutes