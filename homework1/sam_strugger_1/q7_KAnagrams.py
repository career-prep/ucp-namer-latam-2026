# this is a two arrays/strings increment/decrement hashmap counts problem
# Space complexity is O(n+m) and time complexity of O(k) where k is the number of unique characters

from collections import Counter
def main():
    test1 = kAnagrams("apple","peach", 1)
    print(test1)

    test2 = kAnagrams("apple","peach",2)
    print(test2)

    test3 = kAnagrams("apple","peach",0)
    print(test3)

    test4 = kAnagrams("debit curd", "bad credit", 1)
    print(test4)

    test5 = kAnagrams("apple", "appply", 1)
    print(test5)


def kAnagrams(str1,str2,k):

    if k < 0:
        return "Invalid k value"

    str1_count = Counter(str1.lower())
    str2_count = Counter(str2.lower())

    requirements = len(str1_count)
    requirements_met = 0

    for key in str1_count:
        if key in str2_count:
            if str2_count[key] == str1_count[key]:
                requirements_met += 1

    return requirements-requirements_met <= k


main()
# this took me 14 minutes to solve

