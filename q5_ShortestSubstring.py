# Time: 40 minutes
# Technique: forward two pointers 
def ShortestSubstring(a,b):
    need = {}
    for i in range(len(b)):
        need[b[i]] = need.get(b[i],0) + 1

    have = {}
    min_length = 10000000
    matched = 0
    result = ""
    l = 0

    for r in range(len(a)):
        char = a[r]
        have[char] = have.get(char, 0) + 1
        
        if char in need and have[char] == need[char]:
            matched += 1

        while matched == len(need):
            if (r - l + 1) < min_length:
                min_length = r - l + 1
                result = a[l:r+1]
    
            have[a[l]] -= 1
            if a[l] in need and have[a[l]] < need[a[l]]:
                matched -= 1
            l+=1

    return len(result)


print(ShortestSubstring("abracadabra","abc")) #brac 4
print(ShortestSubstring("zxycbaabcwxyzzxwdcbxyzbccbazyx","zzyzx")) #zzxwdcbxyz 10
print(ShortestSubstring("dog","god")) #dog 3