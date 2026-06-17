# # Technique used: brute force method
from collections import Counter


def containsRequired(substring, subCount):
    subStringCount = Counter(substring)
    for char,count in subCount.items():
        if subStringCount.get(char,0) < count:
            return False
    return True

# the string returned has to be greater than or equal to the length of str having the required characters
def shortestSubString(s: str, sub: str) -> int:
    if len(s) == 0 or len(sub) == 0:
        return 0
   
    
    subCount = Counter(sub)
    minCount = float('inf')
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            substring = s[i:j+1]
            
            if containsRequired(substring, subCount):
                minCount = min(minCount, len(substring))
    # assumption made: if it doesn't exist return -1
    return minCount if minCount != float('inf') else -1

print("shortestSubString Results:")
test_cases = [
["abracadabra","abc"],
["zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx"],
["dog", "god"],
["", ""],
["dog", ""],
["d", "dog"],
["defgh", "abd"],
["", "dog"]
            ]
for test_case in test_cases:
    print(shortestSubString(test_case[0], test_case[1])) #Expected Output: 4,10,3,0,0,0



# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Time Taken: 38 mins