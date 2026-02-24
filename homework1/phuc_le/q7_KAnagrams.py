'''
    Hashing technique:

    Maintain a hashmap of elements in one of the string
    If there is a matching char in t, decrement the hashmap
    Calculate the missing char that needed in t
    Check if <= k

    Time: O(n)
    Space: O(n)
    n: numbers of characters in t

    Time spent: 30 mins
'''

from collections import Counter

def KAnagrams(s: str, t: str, k: int) -> bool:
    # Edge case: Not same length
    if len(s) != len(t):
        return False

    freq_map = Counter(s)

    for c in t:
        if c in freq_map:
            freq_map[c] -= 1
    
    # Can only edit 1 string, calculate the numbers of missing characters for s
    need = 0
    for val in freq_map.values():
        if val > 0:
            need += val

    return need <= k


s, t = "apple", "peach"
k = 1
print(KAnagrams(s, t, k))
s, t = "apple", "peach"
k = 2
print(KAnagrams(s, t, k))
s, t = "apple", "peach"
k = 3
print(KAnagrams(s, t, k))
s, t = "debit curd", "bad credit"
k = 1
print(KAnagrams(s, t, k))
s, t = "baseball", "basketball"
k = 2
print(KAnagrams(s, t, k))