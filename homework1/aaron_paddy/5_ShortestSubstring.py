#Time Complexity: O(N + M) Space Complexity: O(N + M)
#Technique Used: Variable size sliding window

from collections import Counter

def shortest_substring(s, req) -> int:
    if not s or not req:
        return 0

    target_counts = Counter(req)
    required_total = len(target_counts)
    
    window_counts = {}
    formed = 0
    
    left = 0
    min_len = float('inf')
    
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
        while left <= right and formed == required_total:
            min_len = min(min_len, right - left + 1)
            left_char = s[left]
            window_counts[left_char] -= 1
            
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            
            left += 1
            
    return min_len if min_len != float('inf') else 0


def test_cases():
    assert shortest_substring("abracadabra", "abc") == 4

    s2 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
    req2 = "zzyzx"
    assert shortest_substring(s2, req2) == 10
    assert shortest_substring("dog", "god") == 3
    assert shortest_substring("hello", "xyz") == 0
    assert shortest_substring("aaaaabc", "abc") == 3

    print("All tests passed successfully!")

test_cases()

#Time spent: 38 mins