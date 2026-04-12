'''
    Store each element in the map as unique key
    Return the string contains all the keys

    n: numbers of characters of the string
    Time: O(n)
    Space: O(n)

    Spend around 10 minutues
'''

def FirstOccurrence(s: str) -> str:
    foundChar = {}
    for char in s:
        if char not in foundChar :
            foundChar[char] = 1
    return "".join(foundChar .keys())

s = "abracadabra"
print(FirstOccurrence(s))
s = "Uber Career Prep"
print(FirstOccurrence(s))
s = "zzyzx"
print(FirstOccurrence(s))