#time complexity: O(n)
#data structure: Stack

def ReverseWords(words):
    word = []

    result = []
    for i in range(len(words)-1, -1, -1):
        if words[i] == ' ':
            while word:
                result.append(word.pop())
            result.append(' ')
        else:
            word.append(words[i])
    while word:
        result.append(word.pop())
    
    return ''.join(result)

#testcases
phrase = "Uber Career Prep"
print(f'test1: {ReverseWords(phrase)}')

phrase = "Emma lives in Brooklyn, New York."
print(f'test2: {ReverseWords(phrase)}')

phrase = ' '
print(f'test3: {ReverseWords(phrase)}')

#time spent: 20 mins