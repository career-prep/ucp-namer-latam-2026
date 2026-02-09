# time: O(n)
# space: O(n)
"""
Two strings are considered to be "k-anagrams" if they can be made into anagrams by changing at most k characters 
in one of the strings. Given the two strings and integer k, determine if they are k-anagrams.

Examples:
Input Strings: "apple", "peach"
Input k: 1
Output: False

Input Strings: "apple", "peach"
Input k: 2
Output: True

Input Strings: "cat", "dog"
Input k: 3
Output: True

Input Strings: "debit curd", "bad credit"
Input k: 1
Output: True

Input Strings: "baseball", "basketball"
Input k: 2
Output: False
"""


def kAnagram(str1, str2, k):
    if len(str1) != len(str2):
        return False

    map = {}
    counter = 0

    for i in range(len(str1)):
        map[str1[i]] = map.get(str1[i], 0) + 1

    for i in range(len(str2)):
        if map.get(str2[i], 0) > 0:
            map[str2[i]] -= 1

        else:
            counter += 1

    return counter <= k


print(kAnagram("apple", "peach", 1))  # false
print(kAnagram("apple", "peach", 2))  # true
print(kAnagram("cat", "dog", 3))  # true
print(kAnagram("debit curd", "bad credit", 1))  # True
print(kAnagram("baseball", "basketball", 2))  # false

# time: 19 minutes
