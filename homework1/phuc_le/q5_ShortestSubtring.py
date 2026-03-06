'''
    Two pointers & Hashing techinque:

    Sliding window technique
    Keep track of the elements in the window
    Store the required char in a hashmap
    If the window contains all needed elements at a right amount, shrink the window
    Else continue to move the window

    Time: O(n + m)
    Space: O(m)
    n, m: lengths of the 2 given strings

    Time spent: 35 mins
'''
from collections import Counter

def ShortestSubtring(a: str, b: str) -> int:
    neededChar = Counter(b)
    findTotal = len(b)
   
    l = 0
    min_len = float("inf")

    for r, c in enumerate(a):
        # If c is in b
        if neededChar[c] > 0:
            findTotal -= 1
        # Decrease the value in the map
        neededChar[c] -= 1
        # IF the all the chars in the window, shrink the window
        while findTotal == 0:
            min_len = min(min_len, r - l + 1)
            # Shrink the window
            neededChar[a[l]] += 1
            # If the window no longer valid
            if neededChar[a[l]] > 0:
                findTotal += 1
            l += 1
    
    return min_len if min_len != float("inf") else 0

a, b = "abracadabra", "abc"
print(ShortestSubtring(a, b))
a, b = "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"
print(ShortestSubtring(a, b))
a, b = "dog", "god"
print(ShortestSubtring(a, b))
