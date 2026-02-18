# Given a string and a second string representing required characters, return the 
# length of the shortest substring containing all the required characters.

# Examples:

# Input Strings: "abracadabra", "abc"
# Output: 4
# (Shortest Substring: "brac")

# Input Strings: "zxycbaabcdwxyzzxzxywdcbxyzabccbazyx", "zzyzx"
# Output: 10
# (Shortest Substring: "zzxwdcbxyz")

# Input Strings: "dog", "god"
# Output: 3
# (Shortest Substring: "dog")

def shortest_substring(s, required):
    if not required or not s:
        return 0
    
    required_count = {}
    for char in required:
        required_count[char] = required_count.get(char, 0) + 1
    
    window_count = {}
    min_len = float('inf')
    left = 0
    formed = 0
    required_len = len(required_count)
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in required_count and window_count[char] == required_count[char]:
            formed += 1
        
        while left <= right and formed == required_len:
            min_len = min(min_len, right - left + 1)
            char = s[left]
            window_count[char] -= 1
            if char in required_count and window_count[char] < required_count[char]:
                formed -= 1
            left += 1
    
    return min_len if min_len != float('inf') else 0


print(shortest_substring("abracadabra", "abc"))
print(shortest_substring("zxycbaabcdwxyzzxzxywdcbxyzabccbazyx", "zzyzx"))
print(shortest_substring("dog", "god"))
print(shortest_substring("aabbcc", "abc"))
