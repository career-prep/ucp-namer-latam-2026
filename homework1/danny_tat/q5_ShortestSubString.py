# time: O(n)
# space: O(n)

"""
Given a string and a second string representing required characters, return the length of the shortest substring containing all the 
required characters.

Examples:
Input Strings: "abracadabra", "abc"

Output: 4
(Shortest Substring: "brac")

Input Strings: "zxycbaabcdwxyzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)

Output: 10
(Shortest Substring: "zzxwdcbxyz")

Input Strings: "dog", "god"
Output: 3
(Shortest Substring: "dog")

"""


def shortestSub(str1, str2):
    if not str2:
        return 0

    countT, window = {}, {}
    for char in str2:
        countT[char] = 1 + countT.get(char, 0)

    have, need = 0, len(countT)
    resLen = float("infinity")
    left = 0

    for right in range(len(str1)):
        char = str1[right]
        window[char] = 1 + window.get(char, 0)
        if char in countT and window[char] == countT[char]:
            have += 1

        while have == need:
            resLen = min(resLen, right - left + 1)
            left_char = str1[left]
            window[left_char] -= 1

            if left_char in countT and window[left_char] < countT[left_char]:
                have -= 1

            left += 1

    return resLen if resLen != float("infinity") else 0


print(shortestSub("abracadabra", "abc"))
print(shortestSub("zxycbaabcdwxyzxwdcbxyzabccbazyx", "zzyzx"))
print(shortestSub("dog", "god"))

# time: 40 minutes
