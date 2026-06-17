#Time: O(R * C), where R and C are the rows and columns respectively
#Space: O(R * C)

def largest_square_of_ones(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * cols for _ in range(rows)]

    max_size = 0

    for i in range(rows):
        for j in range(cols):

            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]

            elif matrix[i][j] == 1:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      
                    dp[i][j-1],      
                    dp[i-1][j-1]     
                )

            else:
                dp[i][j] = 0

            max_size = max(max_size, dp[i][j])

    return max_size

#Time-taken: 30 minutes


import unittest


class TestLargestSquareOfOnes(unittest.TestCase):

    def test_all_ones(self):
        self.assertEqual(largest_square_of_ones([[1, 1], [1, 1]]), 2)

    def test_mixed_matrix(self):
        self.assertEqual(largest_square_of_ones([[1, 1, 0], [1, 1, 0], [0, 0, 0]]), 2)

    def test_empty_matrix(self):
        self.assertEqual(largest_square_of_ones([]), 0)


if __name__ == "__main__":
    unittest.main()