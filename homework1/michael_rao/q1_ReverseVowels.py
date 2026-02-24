# method: forward backward two pointer
# time: O(n)
# space: O(1)

from tabnanny import check


def reverseVowels(string):
    vowel_list = set("aeiouAEIOU")

    res = list(string)
    l = 0
    r = len(string)-1
    while l < r:
        while l < len(string)-1 and string[l] not in vowel_list:
            l += 1
        while r > 0 and string[r] not in vowel_list:
            r -= 1
        if string[l] in vowel_list and string[r] in vowel_list:
            res[l], res[r] = res[r], res[l]
        l += 1
        r -= 1

    return "".join(res)

def checkSolution(string, correct):
    print("Input String:", string)
    print("Correct:", correct)
    print("Output: ", reverseVowels(string))
    print()

checkSolution("Uber Career Prep", "eber Ceraer PrUp")
checkSolution("xyz", "xyz")
checkSolution("flamingo", "flominga")
checkSolution("Aeiou", "uoieA")

# time taken: 15 min