# O(n) time complexity where n is the length of the original string
# O(n) space complexity because we create a set and a new string which in worst case will contain all chars from the original string

str1 = "abracadabra"
str2 = "Uber Career Prep"
str3 = "zzyzx"

def FirstOccurrence(string):
    new = []

    seen = set()

    for char in string:

        if char not in seen:
            new.append(char)
            seen.add(char)

    return "".join(new)

print(FirstOccurrence(str1))
print(FirstOccurrence(str2))
print(FirstOccurrence(str3))


# 27 minutes