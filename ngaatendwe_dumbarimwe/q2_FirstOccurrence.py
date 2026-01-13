#Time: O(n)
#Space: O(n), where n is the length of text 

import unittest

def first_occurrence(text: str) -> str:
    seen = set()
    res = ""
    for char in text:
        if char not in seen:
            res += char
            seen.add(char)
        else:
            continue
    return res 

#Tests
class TestFirstOccurrence(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(first_occurrence("Netherlands"), "Nethrlands")

    def test_all_unique(self):
        self.assertEqual(first_occurrence("fghijk"), "fghijk")

    def test_empty_string(self):
        self.assertEqual(first_occurrence(""), "")

    def test_all_duplicates(self):
        self.assertEqual(first_occurrence("ccccc"), "c")

    def test_special_characters(self):
        self.assertEqual(first_occurrence("k!g!$?k"), "k!g$?")

if __name__ == "__main__":
    unittest.main()
    
#Time taken: 15 minutes
