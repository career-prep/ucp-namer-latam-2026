# This is O(n) time and space complexity
def reverseWords(word):
    return " ".join(word.split()[::-1])

test1 = reverseWords("I am Batman")
print(test1)

# This took me a couple minutes 
