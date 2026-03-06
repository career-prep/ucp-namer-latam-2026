"""
Given a string and a second string representing required characters, 
return the length of the shortest substring containing all the required characters.

Examples:
Input: "abracadabra", "abc" -> Output: 4
Input: "zxycbaabcdwxyzxxwdcbxyzabccbazyx", "zzzyx" -> Output: 10
Input: "dog", "god" -> Output: 3
"""

from collections import Counter

def shortestSubstring(s, required):
    if not s or not required:
        return 0
    
    required_freq = Counter(required)
    needed = len(required_freq)
    
    window_freq = {}
    matched = 0
    left = 0
    min_length = float('inf')
    
    for right in range(len(s)):
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        if char in required_freq and window_freq[char] == required_freq[char]:
            matched += 1
        
        while matched == needed:
            min_length = min(min_length, right - left + 1)
            
            left_char = s[left]
            window_freq[left_char] -= 1
            
            if left_char in required_freq and window_freq[left_char] < required_freq[left_char]:
                matched -= 1
            
            left += 1
    
    return min_length if min_length != float('inf') else 0

# Time Complexity: O(n)
# Space Complexity: O(k) where k is number of unique characters


test_cases = [
    ("abracadabra", "abc"),
    ("zxycbaabcdwxyzxxwdcbxyzabccbazyx", "zzzyx"),
    ("dog", "god")
]

for s, required in test_cases:
    print(shortestSubstring(s, required))
