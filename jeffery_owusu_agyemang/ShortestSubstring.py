# Question 5 (Shortest Substring)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 33 mins

from collections import Counter

def shortestSubstring(s, t):
    if not s or not t:
        return 0

    need = Counter(t)      
    window = Counter()     
    have = 0
    need_count = len(need)

    left = 0
    res_len = float("inf")

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            res_len = min(res_len, right - left + 1)

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                have -= 1

            left += 1

    if res_len == float("inf"):
        return 0
    else:
      return res_len
    


#Tests

# Q5 Tests
print(shortestSubstring("ADOBECODEBANC", "ABC"))  # 4
print(shortestSubstring("a", "a"))                # 1
print(shortestSubstring("a", "aa"))               # 0
print(shortestSubstring("ab", "b"))               # 1
print(shortestSubstring("", "a"))                 # 0

