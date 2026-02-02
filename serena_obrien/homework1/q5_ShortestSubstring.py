# Time complexity: O(n)
# Space complexity: O(m), where m is the number of unique characters in requiredChars

# Technique: Variable-size sliding window

def ShortestSubstring(s, requiredChars):
    if not s or not requiredChars:
        return 0

    minLength = float("inf")
    required = {}
    for char in requiredChars:
        required[char] = required.get(char, 0) + 1
    currWindowCounts = {char: 0 for char in required.keys()}
    progress = 0
    complete = len(required) # number of unique characters in requiredChars

    left = 0
    for right in range(0, len(s)):
        currChar = s[right]

        if currChar in required:
            currWindowCounts[currChar] += 1
            if currWindowCounts[currChar] == required[currChar]:
                progress += 1

        while progress == complete:
            minLength = min(minLength, right - left + 1)

            leftChar = s[left]
            if leftChar in required:
                currWindowCounts[leftChar] -= 1
                if currWindowCounts[leftChar] < required[leftChar]:
                    progress -= 1
        
            left += 1

    if minLength == float("inf"):
        return None
    return minLength

if __name__ == '__main__':
    # inputStr = "abracadabra"
    # requiredChars = "abc"
    inputStr = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
    requiredChars = "zzyzx"
    # inputStr = "do"
    # requiredChars = "god"
    # inputStr = ""
    # requiredChars = ""
    print("Input Strings:", inputStr, ',', requiredChars)
    print("Output:", ShortestSubstring(inputStr, requiredChars))

# ~ time spent: 35 minutes