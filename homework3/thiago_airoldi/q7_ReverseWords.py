# Stack
# O(n) Time Complexity where 'n' is the size of the given string. From splitting and looping through each word.
# O(n) Space Complexity where n is the size of the given string. (From the stack, storing words, and the result array)
# Given a string, return a string with the order of space-separated words reversed


def ReverseWords(sentence):

    if not sentence:
        return ""
    
    # Split the string based on spaces
    arrayOfWords = sentence.split(" ")
    
    # Use a stack to reverse order of the words
    stack = []

    for word in arrayOfWords:
        stack.append(word)

    
    reversedSentence = []

    # Pop the words to build the reversed result
    while stack:
        reversedSentence.append(stack.pop())

        if len(stack) > 0:
            reversedSentence.append(" ")

    return "".join(reversedSentence)


# 5 minutes

# Test Cases


sentence1 = "Uber Career Prep"
sentence2 = "Emma lives in Brooklyn, New York."
sentence3 = ""
sentence4 = "Yo"
sentence5 = "Hey .     Ya"

print(ReverseWords(sentence1))
print(ReverseWords(sentence2))

# My Added Test Cases
print(ReverseWords(sentence3))
print(ReverseWords(sentence4))
print(ReverseWords(sentence5))


