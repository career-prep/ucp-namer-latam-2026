# method: two strings increment decrement hashmap counts
# time: O(n)
# space: O(1)

from collections import Counter
from math import inf

def shortestSubstring(str1, str2):
    map1 = {}
    map2 = Counter(str2)
    ch1 = 0  # how many chars in str1 window that are same as str2
    ch2 = len(map2)
    
    shortest = inf
    shortestL = 0

    l = 0
    for r, chR in enumerate(str1):
        if chR in map2:
            map1[chR] = 1 + map1.get(chR, 0)
            if map1[chR] == map2[chR]:
                ch1 += 1
        
        while ch1 == ch2 and l <= r:
            if r + 1 - l < shortest:
                shortest = r + 1 - l
                shortestL = l
            chL = str1[l]
            if chL in map2:
                map1[chL] -= 1
                if map1[chL] < map2[chL]:
                    ch1 -= 1
            l += 1
    
    return shortest, str1[shortestL:shortestL+shortest]

def checkSolution(str1, str2, correct, substr):
    print("Input Strings:", str1, ",", str2)
    print("Correct:", correct)
    print("Correct:", substr)
    output1, output2 = shortestSubstring(str1,str2)
    print("Output: ", output1)
    print("Output: ", output2)
    print()

checkSolution("abracadabra","abc",4,"brac")
checkSolution("zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx",10,"zzxwdcbxyz")
checkSolution("dog","god",3,"dog")

# time taken: 40 min