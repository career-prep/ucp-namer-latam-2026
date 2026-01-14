#Samaksh Arora
#UniqueSum
#Time Complexity: O(n)
#Space Complexity: O(n)

def firstOccurrence(text):
    seen = {}
    newString = ''
    for letter in text:
        if letter not in seen:
            seen[letter] = 1
            newString += letter
        else:
            continue
    return newString


testString = "abracadabra"
print(firstOccurrence(testString)) #output: "abrcd"

testString2 = "Uber Career Prep"
print(firstOccurrence(testString2)) #output: "Uber CaPp"

testString3 = "zzyzx"
print(firstOccurrence(testString3)) #output: "zyx"

#Time Spent: 7 minutes