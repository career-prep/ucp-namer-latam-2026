''' Question 5: ShortestSubstring
Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.
Examples:          lr
Input Strings: "abracadabra", "abc"
Output: 4
(Shortest Substring: "brac")
Input Strings: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the
Mojave Desert in California!)
Output: 10
(Shortest Substring: "zzxwdcbxyz")
Input Strings: "dog", "god"
Output: 3
(Shortest Substring: "dog")
'''

# Time Complexity: O(n). As each character is visited at most twice — once by end, once by start and the 
# Space Complexity: O(1)

def shortestSubstring(s, required):
    if not s or not required or len(s) < len(required):
        return 0

    map = [0] * 128
    count = len(required)
    start = 0
    end = 0
    min_len = float('inf')

    for char in required:
        map[ord(char)] += 1

    while end < len(s):
        if map[ord(s[end])] > 0:
            count -= 1
        map[ord(s[end])] -= 1
        end += 1

        while count == 0:
            if end - start < min_len:
                min_len = end - start

            if map[ord(s[start])] == 0:
                count += 1
            map[ord(s[start])] += 1
            start += 1

    return 0 if min_len == float('inf') else min_len

print(shortestSubstring("abracadabra", "abc"))
print(shortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
print(shortestSubstring( "dog", "god"))