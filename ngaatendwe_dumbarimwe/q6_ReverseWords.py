#Time: O(n), where n is length of text
#Space: O(n)

import unittest

def reverse_words(text:str) -> str:

    text_lst = text.split(sep=" ")
    left = 0
    right = len(text_lst) - 1

    while left < right:
        text_lst[left], text_lst[right] = text_lst[right], text_lst[left]
        left += 1
        right -= 1

    return " ".join(text_lst)


#Tests
class TestReverseWords(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(reverse_words("I love Python"), "Python love I")

    def test_single_word(self):
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_multiple_spaces_words(self):
        self.assertEqual(reverse_words("one two three four"), "four three two one")


if __name__ == "__main__":
    unittest.main()

#Time-taken: 15 minutes