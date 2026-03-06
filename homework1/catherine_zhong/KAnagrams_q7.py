#time complexity: O(n)
#space complexity: O(n)

def KAnagrams(str1, str2, k):
    str1Chars = dict()
    diff = len(str1)

    #assuming letters cannot be added
    if len(str1) != len(str2):
        return False

    #gets all characters of string1 
    for i in str1:
        str1Chars[i] = str1Chars.get(i, 0) + 1
    
    #checks characters in string2
    for i in str2:
        if str1Chars.get(i, 0) > 0:
            str1Chars[i] = str1Chars.get(i) -1
            diff -= 1
        
    #checks if difference is smaller than k
    if diff <= k:
        return True
    return False

test1A = 'apple'
test1B = 'peach'
k1 = 2
test2A = 'cat'
test2B = 'dog'
k2 = 3
test3A = 'debit curb'
test3B = 'bad credit'
k3 = 2
test4A = ''
test4B = ''
k4 = 1
test5A = 'baseball'
test5B = 'basketball'
k5 = 2

print('test1: ', KAnagrams(test1A, test1B, k1))
print('test2: ', KAnagrams(test2A, test2B, k2))
print('test3: ', KAnagrams(test3A, test3B, k3))
print('test4: ', KAnagrams(test4A, test4B, k4))
print('test5: ', KAnagrams(test5A, test5B, k5))

#time spent: 20 mins
