#Time: O(m + n)
#Space: O(m + n), where m is the length of text1 and n is the length of text2

import unittest

def string_compare(text1: str, text2: str) -> bool:
    text1_list = []
    text2_list = []

    for l in text1:
        if text1_list and l == "#":
            text1_list.pop()
        else:
            text1_list.append(l)
    
    for l in text2:
        if text2_list and l == "#":
            text2_list.pop()
        else:
            text2_list.append(l)
    
    return text1_list == text2_list


class TestStringCompare(unittest.TestCase):

    def test_both_empty(self):
        self.assertTrue(string_compare("", ""))

    def test_no_backspaces_equal(self):
        self.assertTrue(string_compare("abc", "abc"))

    def test_simple_backspace(self):
        self.assertTrue(string_compare("ab#c", "ad#c"))

    def test_excess_backspaces(self):
        self.assertTrue(string_compare("a##", "#"))

    def test_leading_backspace_not_ignored(self):
        self.assertFalse(string_compare("#a", "a"))

    def test_not_equal(self):
        self.assertFalse(string_compare("a#c", "b"))


if __name__ == "__main__":
    unittest.main()

#Time-taken: 15 minutes