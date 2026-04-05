# Two Pointer: Variable Size Sliding Window
# O(n) Time Complexity where n is the length of the longer input string
# O(1) or I guess O(26) time complexity where 26 is how many indices are in the helper array used

s1, sub1 = "abracadabra", "abc"

s2, sub2 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"

s3, sub3 = "dog", "god"

def ShortestSubstring(s, sub):

    # Create a helper array of 26 indices, representing a latter in the alphabet. The value at each index is how many of that letter we need in the substring.
    needed = [0] * 26

    for i in range(len(sub)):
        c = sub[i]
        idx = ord(c) - ord('a')
        needed[idx] += 1

    # To track how many chars the window is still missing from the second string
    missing = len(sub)

    windowSize = float('inf')

    # Increment r to form a valid window, then increment l to minimize it. For each valid window, update the windowSize if it is smaller than our current smallest
    l = 0

    for r in range(len(s)):

        c = s[r]

        idx = ord(c) - ord('a')

        if needed[idx] > 0:
            # Meaning, we need this char in our window
            missing -= 1

        needed[idx] -= 1

        if missing > 0:
            # Keep scanning
            continue
            
        elif missing == 0:
            # Valid subarray
            windowSize = min(windowSize, (r - l + 1))

            # Decrease window size
            while missing == 0:
                c2 = s[l]

                # Shrink window
                l += 1

                idx2 = ord(c2) - ord('a')

                # Check if the char we excluded was needed
                needed[idx2] += 1

                if needed[idx2] > 0:
                    missing += 1
                else:
                    windowSize = min(windowSize, (r - l + 1))
 

    if windowSize == float('inf'):
        return -1 # Indicating a window could not be found
    else:
        return windowSize


print(ShortestSubstring(s1, sub1))
print(ShortestSubstring(s2, sub2))
print(ShortestSubstring(s3, sub3))

# 21 minutes