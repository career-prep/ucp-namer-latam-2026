#Time: O(n), where n is the largest Catalan number requested
#Space: O(n log n)

def catalan_numbers(n):
    catalan = [0] * (n + 1)

    catalan[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    return catalan

#Time-taken: 30 minutes


import unittest


class TestCatalanNumbers(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(catalan_numbers(0), [1])

    def test_first_few_values(self):
        self.assertEqual(catalan_numbers(4), [1, 1, 2, 5, 14])

    def test_larger_value(self):
        self.assertEqual(catalan_numbers(5)[5], 42)


if __name__ == "__main__":
    unittest.main()