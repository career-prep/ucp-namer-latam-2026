"""
Technique Used: Variable-size sliding window + Two strings increment/decrement hashmap counts
Time Complexity: O(n + m), n and m are the lengths of string and required_str, respectively
Space Complexity: O(K), k = the number of unique characters in the hashmaps
"""

# Input: two strings, one representing required characters
# Output: integer, length of shortest substring
# Approach: Create a frequency map to identify how many unique characters there are in the
# required character string. Increment the right pointer across the entire main string and 
# update another map for every character I encounter. If a character's count in the window
# matches with the required character counts, a character match has been found and increment that
# variable by 1.
# Edge Cases: required character greater length than main string, duplicate characters in 
# required, no valid window exists

def shortest_substring(string: str, required_str: str) -> int:
    if not string or not required_str or len(required_str) > len(string):
        return 0
    
    required_counts = {}

    for char in required_str:
        required_counts[char] = required_counts.get(char, 0) + 1

    required_chars = len(required_counts)

    window_counts = {}
    required_match = 0
    
    left = 0
    min_length = float('inf')

    for right in range(len(string)):
        char = string[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in required_counts and window_counts[char] == required_counts[char]:
            required_match += 1
        
        while left <= right and required_match == required_chars:
            min_length = min(min_length, right - left + 1)

            removed_char = string[left]
            window_counts[removed_char] -= 1

            if removed_char in required_counts and window_counts[removed_char] < required_counts[removed_char]:
                required_match -= 1
            
            left += 1
        
    return min_length if min_length != float('inf') else 0

print(shortest_substring("abracadabra","abc"))
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx"))
print(shortest_substring("dog","god"))

# Time Spent: 40 minutes