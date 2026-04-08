# firstOccurence returns a string that contains only the first occurence of each character in a string. Note: Case-sensetive, so for eg: 'a' and 'A' are considered different
def firstOccurrence(word: str) -> str:
    result = []
    usedSet = set()
    for letter in word:
        if letter not in usedSet:
            result.append(letter)
            usedSet.add(letter)
    return "".join(result)

print("firstOccurence Results:")
test_cases = ["abracadabra", "Uber Career Prep", "zzyzx", "", "z"]
for test_case in test_cases:
    print(firstOccurrence(test_case)) # Expected Output: "abrcd","Uber CaPp", "zyx", "","z"
 
# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 4 minutes