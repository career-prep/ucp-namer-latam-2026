#Time: O(n^3), where n is the length of the length of the input string
#Space: O(n)

def word_break_with_words(s, dictionary):
    dictionary = set(word.lower() for word in dictionary)

    n = len(s)
    s = s.lower()

    dp = [False] * (n + 1)
    prev = [-1] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                prev[i] = j
                break

    if not dp[n]:
        return False

    words = []
    idx = n

    while idx > 0:
        j = prev[idx]
        words.append(s[j:idx])
        idx = j

    words.reverse()

    return True, words


#Time-taken: 30 minutes


import unittest


class TestWordBreakWithWords(unittest.TestCase):

    def test_valid_break(self):
        self.assertEqual(
            word_break_with_words("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
            (True, ["cat", "sand", "dog"]),
        )

    def test_invalid_break(self):
        self.assertFalse(word_break_with_words("catsandog", ["cat", "cats", "and", "sand", "dog"]))

    def test_case_insensitive(self):
        self.assertEqual(word_break_with_words("Hello", ["hello"]), (True, ["hello"]))


if __name__ == "__main__":
    unittest.main()