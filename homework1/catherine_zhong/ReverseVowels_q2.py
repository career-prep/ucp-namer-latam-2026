#time complexity: O(n)
#space complexity: O(n)

def ReverseVowels(phrase):
    charList = list(phrase)
    start = 0
    end = len(phrase)-1
    vowels = 'aeiou'

    while start < end:
        if charList[start].lower() not in vowels:
            start += 1
        if charList[end].lower() not in vowels:
            end -= 1

        if charList[start].lower() in vowels and charList[end].lower() in vowels:
            temp = charList[start]
            charList[start] = charList[end]
            charList[end] = temp
            start +=1 
            end -= 1
    
    return ''.join(charList)

#test cases
test1 = "Uber Career Prep"
test2 = "xyz"
test3 = "aeiou"
test4 = "1234567"
test5 = ""

print('test1: ', ReverseVowels(test1))
print('test2: ', ReverseVowels(test2))
print('test3: ', ReverseVowels(test3))
print('test4: ', ReverseVowels(test4))
print('test5: ', ReverseVowels(test5))

#time spent: 10 mins