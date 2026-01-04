'''
    Store each element in the map as unique key
    Return the string contains all the keys

    n: numbers of characters of the string
    Time: O(n)
    Space: O(n)

    Spend around 5 minutues
'''

def FirstOccurrence(s: str) -> str:
    mp = {}
    for c in s:
        if c not in mp:
            mp[c] = 1
    return "".join(mp.keys())

s = "abracadabra"
print(FirstOccurrence(s))
s = "Uber Career Prep"
print(FirstOccurrence(s))
s = "zzyzx"
print(FirstOccurrence(s))