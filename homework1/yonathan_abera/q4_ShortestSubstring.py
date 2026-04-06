#Variable Size sliding window, One directional running computation
#O(n) time, O(n) space
from collections import defaultdict


def shortest_sub(characters, comparison):
    compare = defaultdict(int)
    for x in comparison:
        compare[x] += 1
    
    window = defaultdict(int)
    left = 0

    matches = 0
    curr_length = 0
    min_length = 10**9
    distinct_matches = len(compare)

    for i in range(len(characters)):
        curr_length += 1
        window[characters[i]] += 1

        if characters[i] in compare and window[characters[i]] == compare[characters[i]]:
            matches += 1
        
        while matches == distinct_matches:
            min_length = min(min_length, curr_length)
            window[characters[left]] -= 1
            curr_length = i - left
            if characters[left] in compare and window[characters[left]] < compare[characters[left]]:
                matches -= 1
            left += 1
    return min_length

print(shortest_sub("abracadabra", "abc")) 
print(shortest_sub("zxycbaabcdwxyzzxwdcbxyzabcobazy", "zzyzx"))
print(shortest_sub("ADOBECODEBANC", "ABC"))
print(shortest_sub("a", "a"))
print(shortest_sub("a", "aa"))
print(shortest_sub("abcdebdde", "bde"))
print(shortest_sub("aaabbbc", "abc"))  

#40 minutes(was most likely overtime)



