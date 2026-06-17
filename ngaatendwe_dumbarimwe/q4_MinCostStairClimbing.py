#Time: O(n), where n is the length of cost
#Space: O(1)

def minCostClimbingStairs(cost: list[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0
 
        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
        
        return curr

#Time-taken: 30 minutes


import unittest


class TestMinCostClimbingStairs(unittest.TestCase):

    def test_two_steps(self):
        self.assertEqual(minCostClimbingStairs([10, 15]), 10)

    def test_example_case(self):
        self.assertEqual(minCostClimbingStairs([10, 15, 20]), 15)

    def test_larger_case(self):
        self.assertEqual(
            minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
        )


if __name__ == "__main__":
    unittest.main()