# Question 5: ShortestSubstring

# Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.

# Examples:

# Input Strings: "abracadabra", "abc"
# Output: 4
# (Shortest Substring: "brac")

# Input Strings: "zxycbaabcdwxyzxxwdcbxyzabccbazyx", "zzzyx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
# Output: 10
# (Shortest Substring: "zzxwdcbxyz")

# Input Strings: "dog", "god"
# Output: 3
# (Shortest Substring: "dog")

from collections import Counter, defaultdict

def ShortestSubstring(text, required_chars):
    if not text or not required_chars:
        return 0

    # Count frequency of required characters
    required_count = Counter(required_chars)
    required_unique = len(required_count)

    # Sliding window
    window_count = defaultdict(int)
    formed = 0  # Number of unique chars in current window with required frequency

    left = 0
    min_len = float('inf')

    for right in range(len(text)):
        char = text[right]
        window_count[char] += 1

        # Check if current char's frequency matches required frequency
        if char in required_count and window_count[char] == required_count[char]:
            formed += 1

        # Try to contract the window while it's valid
        while formed == required_unique:
            # Update minimum length
            min_len = min(min_len, right - left + 1)

            # Remove leftmost character
            left_char = text[left]
            window_count[left_char] -= 1
            if left_char in required_count and window_count[left_char] < required_count[left_char]:
                formed -= 1
            left += 1

    return min_len if min_len != float('inf') else 0



test_cases = [("abracadabra", "abc"), ("zxycbaabcdwxyzxxwdcbxyzabccbazyx", "zzzyx"), ("dog", "god")]
for test_case in test_cases:
    text, required_chars = test_case
    print(ShortestSubstring(text, required_chars))

# Time Complexity = O(n)
# Space Complexity = O(n)

# Spent a total of 40 mins on this question