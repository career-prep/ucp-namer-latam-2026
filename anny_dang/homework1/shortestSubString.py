from collections import Counter
def findShortestSubString(s, requiredStr):
    """
    # Technique used: variable-size (shrinking/growing) sliding window 

    # Idea:
    expand the window until it contains all required characters (including duplicates)
    then shrink from the left while it remains valid, tracking the shortest window 

    # Complexity:
    Time: O(n)
    Space: O(n)

    # Time spent: 30mins
    """
    if not requiredStr:
        return ""
    needed = Counter(requiredStr)
    rStr = set(requiredStr)
    res = ""
    best = float("inf")
    current = 0
    l = 0
    missing = len(requiredStr)

    for r in range(len(s)):
        if s[r] in rStr and needed[s[r]] > 0:
            missing -= 1

        current += 1
        needed[s[r]] -= 1

        while missing == 0 and l <= r:
            if s[l] in rStr and needed[s[l]] == 0:
                if current < best:
                    res = s[l:r+1]
                    best = current 
                missing += 1
            needed[s[l]] += 1
            current -= 1
            l += 1
    return res

s1, r1 = "abracadabra", "abc"
print(findShortestSubString(s1, r1))

s2, r2 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"
print(findShortestSubString(s2, r2))

s3, r3 = "dog", "god"
print(findShortestSubString(s3, r3))
