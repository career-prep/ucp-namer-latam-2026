#Time: O(n)
#Space: O(n), where n is the length of text 

import unittest

def reverse_vowels(text: str) -> str:
    temp = list(text)
    left_p = 0
    right_p = len(temp) - 1
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    

    while left_p < right_p:
        if temp[left_p] in vowels and  temp[right_p] in vowels:
            temp[left_p], temp[right_p] = temp[right_p], temp[left_p]
            left_p += 1
            right_p -= 1
        
        while left_p < len(text) and temp[left_p] not in vowels:
            left_p += 1

        while right_p >= 0 and temp[right_p] not in vowels:
            right_p -= 1
        
    return ''.join(temp)


class TestReverseVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(reverse_vowels("bcdfg"), "bcdfg")

    def test_single_vowel(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_multiple_vowels(self):
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")

    def test_mixed_case_vowels(self):
        self.assertEqual(reverse_vowels("hElloAp"), "hAlloEp")

    def test_only_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")


if __name__ == "__main__":
    unittest.main()

#Time-taken: 20 minutes