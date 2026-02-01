#time complexity: O(n)
#space complexity: O(n)

def ShortestSubstring(str1, str2):
    chars = dict()
    found = len(str2)

    for i in str2:
        chars[i] = chars.get(i, 0) + 1
    
    end = 0
    while found > 0 and end < len(str1):
        if str1[end] in chars:
            if chars[str1[end]] > 0:
                found -= 1
            chars[str1[end]] = chars[str1[end]] - 1
        end += 1

    start = 0

    while start < end:
        if str1[start] in chars:
            if chars[str1[start]] + 1 > 0:
                return end - start
            chars[str1[start]] = chars[str1[start]] + 1

        start += 1
    
    return end - start



test1A = 'abcdabc'
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