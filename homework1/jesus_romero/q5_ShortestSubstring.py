"""
Time, Space complexities: O(n^2), O(n)
Q5: ShortestSubstring
Given a string and a second string representing required characters, 
return the length of the shortest substring containing all the required characters
"""

def ShortestSubstring(s, subs):
    if not s or not subs:
        return 0

    #1. Manually build the requirement map
    required = {}
    for char in subs:
        required[char] = required.get(char, 0) + 1
    
    #2. Setup window using a hashmap
    window = {}
    left = 0
    min_len = float('inf')

    #Helper function to check if window meets requirements
    def is_valid(window_map, req_map):
        for char, count in req_map.items():
            if window_map.get(char, 0) < count:
                return False
        return True

    #3. Start Sliding
    for right in range(len(s)):
        # Add character at right pointer
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # While the window has everything we nees
        while is_valid(window, required):
            # Calculate current length and update min
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len

            # Remove the leftmost character to try and find a smaller window
            left_char = s[left]
            window[left_char] -= 1
            left += 1

    if min_len != float('inf'): 
        return min_len 
    else: 
        return 0

def test_SS():
    input_strings = ("abracadabra", "abc")
    expected = 4
    result = ShortestSubstring(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("zxycbaabcdwxyzzxwdcbxyzabccbazxyx", "zzyzx")
    expected = 10
    result = ShortestSubstring(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

    input_strings = ("dog", "god")
    expected = 3
    result = ShortestSubstring(input_strings[0], input_strings[1])
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_SS()