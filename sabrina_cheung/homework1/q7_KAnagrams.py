"""
Technique Used: One directional running computation
Time Complexity: O(n)
Space Complexity: O(k)


"""
from collections import defaultdict

def KAnagrams(string1, string2, k):
    if len(string1) != len(string2):
        return False
    dic = defaultdict(int)
    
    for i in string1:
        dic[i] += 1

    for i in string2:
        dic[i] -= 1
    
    change = sum(v for v in dic.values() if v > 0)
    return change <= k

test = [('apple', 'peach', 1),
        ('apple', 'peach', 2),
        ('cat', 'dog', 3),
        ('debit curd', 'bad credit', 1),
        ('baseball', 'basketball', 2)]

for i in test:
    print(KAnagrams(i[0], i[1], i[2]))
# Time Spent: 25 mins