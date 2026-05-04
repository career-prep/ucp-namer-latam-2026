# Reverse Words
# Data Structure: Stack
# Time Complexity: O(N) where N is the number of characters in the string
# Space Complexity: O(W) where W is the number of words in the string


def reverseWords(given_string):
    listOfWords = given_string.split(" ")
    stackOfWords = []

    for word in listOfWords:
        stackOfWords.append(word)
    
    result = []

    while stackOfWords:
        result.append(stackOfWords.pop())
    
    return " ".join(result)

print(reverseWords("Uber Career Prep"))               # expected: "Prep Career Uber"
print(reverseWords("Emma lives in Brooklyn, New York."))  # expected: "York. New Brooklyn, in lives Emma"
print(reverseWords("hello"))                          # expected: "hello"
print(reverseWords("a b c d"))                        # expected: "d c b a"
