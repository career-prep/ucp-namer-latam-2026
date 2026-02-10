from collections import Counter

def shortest_substring_length(s: str, required: str) -> int:
    """
    Return the length of the shortest substring of `s` that contains
    all characters in `required` (including duplicates).

    Example:
        s="abracadabra", required="abc" -> 4 ("brac")

    Time Complexity: O(n)
        - Each pointer (left/right) moves across the string at most once.
    Space Complexity: O(m)
        - m is the number of distinct required characters stored in a map.
    """

    # Count how many of each required character we need
    need = Counter(required)
    need_types = len(need)  # number of distinct chars we must satisfy

    # Sliding window counts for characters currently in the window
    window = {}

    have_types = 0  # how many distinct chars currently satisfy the needed count
    best = float("inf")

    left = 0
    for right, ch in enumerate(s):
        # Expand window by including s[right]
        window[ch] = window.get(ch, 0) + 1

        # If this character is required and we just reached the needed amount,
        # we satisfied one required "type"
        if ch in need and window[ch] == need[ch]:
            have_types += 1

        # While the window contains everything we need, try shrinking it
        while have_types == need_types:
            best = min(best, right - left + 1)

            # Shrink from the left
            left_char = s[left]
            window[left_char] -= 1

            # If we removed a required char and now we have too few of it,
            # the window is no longer valid
            if left_char in need and window[left_char] < need[left_char]:
                have_types -= 1

            left += 1

    # If we never found a valid window, return 0 (or you can return -1 if preferred)
    return 0 if best == float("inf") else best


# Examples
print(shortest_substring_length("abracadabra", "abc"))  # 4
print(shortest_substring_length("zxycbaabcdwxyzzxwdcbxyzabccbazxy", "zzyzx"))  # 10
print(shortest_substring_length("dog", "god"))  # 3

