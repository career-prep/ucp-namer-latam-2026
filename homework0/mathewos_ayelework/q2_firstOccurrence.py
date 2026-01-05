def firstOccurrence(word):
    result = ""
    usedSet = set()
    for letter in word:
        if letter not in usedSet:
            result += letter
            usedSet.add(letter)
    return result
word = "zzyzx"
print(firstOccurrence(word))

# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 4 minutes