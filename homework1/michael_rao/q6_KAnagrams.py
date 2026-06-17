# method: two strings hashmap counts
# time: O(n)
# space: O(1)

from collections import Counter
from tabnanny import check

def kAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    
    map1 = Counter(str1)
    map2 = Counter(str2)
    changes = 0

    for ch in map1:
        if map1[ch] > map2.get(ch,0):
            changes += map1[ch] - map2.get(ch,0)
    
    return changes <= k

def checkSolution(str1,str2,k,correct):
    print("Input Strings:", str1, ",", str2)
    print("Input k:", k)
    print("Correct:", correct)
    print("Output: ", kAnagrams(str1,str2,k))
    print()

checkSolution("apple", "peach", 1, False)
checkSolution("apple", "peach", 2, True)
checkSolution("cat","dog",3,True)
checkSolution("debit curd", "bad credit", 1, True)
checkSolution("baseball","basketball",2,False)

# time taken: 10 min