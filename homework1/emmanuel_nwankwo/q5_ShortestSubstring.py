# Technique: Sliding window
# Time Complexity: O(n + m)
# Space Complexity: O(m)

from collections import Counter, defaultdict

def shortest_substring(s, t):
    need = Counter(t)
    have = defaultdict(int)
    left = 0
    required = len(need)
    formed = 0

    best_len = float("inf")

    for right, char in enumerate(s):
        have[char] += 1

        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len

            left_ch = s[left]
            have[left_ch] -= 1

            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1

            left += 1

    return 0 if best_len == float("inf") else best_len

print(shortest_substring("abracadabra", "abc"))
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
print(shortest_substring("dog", "god"))

# My Edge Testcases:
print(shortest_substring("aaaaa", "aa")) # all same char

# Time Taken: 21mins 9secs