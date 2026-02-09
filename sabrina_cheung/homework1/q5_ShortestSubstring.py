"""
Technique Used: grow shrink 2 pointer
Time Complexity: O(n)
Space Complexity: O(k)

Intuition: Use the grow shrink two pointer method to find the substring that contains the target letters.
One pointer starts at index 0, the other moves forward until a substring is reached. Store the length in a variable.
Then move the first pointer forward to see if a shorter length substring can be found.
Repeat til pointers reach the end.
"""

def ShortestSubstring(string, target):
    point1 = 0
    point2 = 0
    length = float('inf')
    have = {}
    need = {}

    for i in target:
        have[i] = 0
        need[i] = need.get(i, 0) + 1
    formed = 0
    required = len(need)

    while point2 < len(string):
        while formed != required and point2 < len(string):
            char = string[point2]
            if char in have:
                have[char] += 1
                if have[char] == need[char]:
                    formed += 1
            point2 += 1
        
        while formed == required:
            if point2 - point1 < length:
                length = point2 - point1
            char = string[point1]
            if char in have:
                have[char] -= 1
                if have[char] < need[char]:
                    formed -= 1
            point1 += 1
    return length



test = [('abracadabra', 'abc'),
        ('dog', 'god'),
        ('oheloo', 'oo'),
        ('abxasfjdslkwionjkdadbdfhjr', 'as')]

for i in test:
    print(ShortestSubstring(i[0], i[1]))
# Time Spent: 40 mins