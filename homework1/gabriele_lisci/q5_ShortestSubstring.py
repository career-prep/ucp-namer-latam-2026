# Technique: Variable sliding window
# Runtime: O(n)
# Space complexity: O(n)

from collections import Counter


def ShortestSubstring(word, subWord):
    subWordDict = Counter(subWord)
    foundDict = {}
    need = len(subWordDict)
    count = 0
    left, right = 0, 0
    n = len(word)
    minCount = float('inf')
    while right < n:
        leftChar = word[left]
        rightChar = word[right]
        if rightChar in subWordDict:
            foundDict[rightChar] = foundDict.get(rightChar, 0) + 1
            if subWordDict[rightChar] == foundDict[rightChar]:
                count += 1
        while count == need:
            minCount = min(minCount, right - left + 1)
            if leftChar in subWordDict:
                foundDict[leftChar] -= 1
                if subWordDict[leftChar] > foundDict[leftChar]:
                    count -= 1
            left += 1
            leftChar = word[left]
        right += 1
    return minCount

print(ShortestSubstring("abracadabra", "abc") == 4)
print(ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx") == 10)
print(ShortestSubstring("dog", "god") == 3)



# Time spent: 40:00
# Had a hard time with this one
