#Time: O(n * n), where n is the length of text1
#Space: O(k),  where k is the number of unique characters in text2

from collections import Counter
import unittest

def shortest_substring(text1:str, text2:str) -> int:
    min_length = float("inf")
    

    for i in range(len(text1)):
        p2 = i
        counts = Counter(text2)
        while p2 < len(text1):
            if text1[p2] in counts:
                counts[text1[p2]] -= 1
                if counts[text1[p2]] == 0:
                    del counts[text1[p2]]
                if not counts:
                    min_length = min(min_length, p2 - i + 1)
            p2 += 1
    return min_length
    


class TestShortestSubstring(unittest.TestCase):

    def test_empty_text1(self):
        self.assertEqual(shortest_substring("", "abc"), float("inf"))

    def test_empty_text2(self):
        self.assertEqual(shortest_substring("abc", ""), float("inf"))

    def test_exact_match(self):
        self.assertEqual(shortest_substring("abc", "abc"), 3)

    def test_basic_case(self):
        self.assertEqual(shortest_substring("adobecodebanc", "abc"), 4)

    def test_repeated_characters(self):
        self.assertEqual(shortest_substring("aaab", "aab"), 3)

    def test_no_valid_substring(self):
        self.assertEqual(shortest_substring("abc", "d"), float("inf"))


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 min 