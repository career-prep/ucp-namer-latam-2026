"""
Time, Space complexities: O(n), O(n)

Q2: Reverse Vowels
Given a string, reverse the order of the vowels in the string
"""

def reverseVowels(s):
    #1. Create needed variables, a list of all characters in the string, 
    # two pointers, and a set with all vowels 

    s_list = list(s)
    low = 0
    high = len(s) - 1
    vowels = set("aeiouAEIOU")

    #2. Iterate while the two pointers don't meet
    while low < high:
        #3. If low is not a vowel, move right
        if s_list[low] not in vowels:
            low += 1
        #4. if high is not a vowel, move left
        elif s_list[high] not in vowels:
            high -= 1
        #5. If both are vowels, swap them and move both respectively 
        else:
            temp = s_list[low]
            s_list[low] = s_list[high]
            s_list[high] = temp

            low += 1
            high -= 1

    #6. Join the resulting list into a string
    return "".join(s_list)

def test_reverseVowels():
    input_string = "Uber Career Prep"
    expected = "eber Ceraer PrUp"
    result = reverseVowels(input_string)
    assert result == expected, f"Expected {expected}, got {result}"

    input_string = "xyz"
    expected = "xyz"
    result = reverseVowels(input_string)
    assert result == expected, f"Expected {expected}, got {result}"

    input_string = "flamingo"
    expected = "flominga"
    result = reverseVowels(input_string)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_reverseVowels()