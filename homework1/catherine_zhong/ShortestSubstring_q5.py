#time complexity: O(n)
#space complexity: O(n)

def ShortestSubstring(str1, str2):
    #checks for empty strings
    if not str1 or not str2:
        return 0

    charsNeeded = dict()
    for i in str2:
        charsNeeded[i] = charsNeeded.get(i, 0) + 1

    missing = len(str2)
    minLen = float('inf')
    minStart = 0

    start = 0
    end = 0
    for end in range(len(str1)):
        #checks if character is needed
        if str1[end] in charsNeeded:
            if charsNeeded[str1[end]]>0:
                missing -= 1
            charsNeeded[str1[end]] -= 1

        #shrinking
        while missing == 0:
            if end - start + 1 < minLen:
                minLen = end - start + 1
                minStart = start
            if str1[start] in charsNeeded:
                charsNeeded[str1[start]] += 1
                if charsNeeded[str1[start]] > 0:
                    missing += 1

            start += 1
    
    if minLen != float('inf'):
        return minLen
    return 0


test1A = 'abdecab'
test1B = 'abc'
test2A = ''
test2B = ''
test3A = 'dog'
test3B = 'god'
test4A = 'zzxwdcbxyz'
test4B = 'zzyxx'
test5A = 'babscsdbdefxxxxxxxxx'
test5B = 'abcdef'
print('test1: ', ShortestSubstring(test1A, test1B))
print('test2: ', ShortestSubstring(test2A, test2B))
print('test3: ', ShortestSubstring(test3A, test3B))
print('test4: ', ShortestSubstring(test4A, test4B))
print('test5: ', ShortestSubstring(test5A, test5B))
#time spent: 35 mins