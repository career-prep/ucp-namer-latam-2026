# Time: O(n)
# Space: O(n), where n is the length of the strings


from collections import Counter
import unittest

def kAnagrams(text1:str, text2:str , k:int) -> bool:

    if len(text1) != len(text2):
        return False
    
    text2_dict = Counter(text2)

    for letter in text1:
        if letter in text2_dict:
            if text2_dict[letter] > 0:
                text2_dict[letter] -= 1
                if text2_dict[letter] == 0:
                    del text2_dict[letter]
        else:
            if k > 0:
                k -=1
            else:
                return False
    return True

  

class TestKAnagrams(unittest.TestCase):

    def test_different_lengths(self):
        self.assertFalse(kAnagrams("abc", "ab", 1))

    def test_exact_anagram(self):
        self.assertTrue(kAnagrams("listen", "silent", 0))

    def test_k_allows_replacement(self):
        self.assertTrue(kAnagrams("abc", "abd", 1))

    def test_k_insufficient(self):
        self.assertFalse(kAnagrams("abc", "def", 1))

    def test_leftover_characters_ignored(self):
        self.assertTrue(kAnagrams("a", "b", 1))


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 min