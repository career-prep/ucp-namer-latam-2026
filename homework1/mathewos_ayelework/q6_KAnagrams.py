from collections import Counter

def kAnagrams(s1:str,s2: str,k:int) -> bool:
    # assumption, k is a non-negative integer (k >= 0)
    counter = 0
    if len(s1) != len(s2):
        return False
    
    freqMaps1   = Counter(s1)
    freqMaps2   = Counter(s2)
    
    for char,freq in freqMaps1.items():
        counter += abs(freqMaps2.get(char, 0) - freq)
    if counter > k:
        return False
    return True

print("kAnagrams Results:")
test_cases = [
            ["apple", "peach", 1],
            ["apple", "peach", 2],
            ["cat", "dog", 3],
            ["debit card", "bad credit", 1],
            ["baseball", "basketball", 2],
            ["", "", 0],
              ]
for test_case in test_cases:
    print(kAnagrams(test_case[0], test_case[1], test_case[2])) #Expected Output: F,T,T,T,F,T


# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Taken: 25mins