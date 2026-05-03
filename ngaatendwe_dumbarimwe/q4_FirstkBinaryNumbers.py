#Time: O(k)
#Space: O(k)

from collections import deque
import unittest

def first_k_binary(k):
    if k <= 0:
        return []

    result = ["0"]  # start with 0
    queue = deque(["1"])  # start generating from 1

    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)

        queue.append(curr + "0")
        queue.append(curr + "1")

    return result


#Tests
class TestFirstKBinary(unittest.TestCase):

    def test_k_five(self):
        self.assertEqual(first_k_binary(5), ["0","1","10","11","100"])

    def test_k_one(self):
        self.assertEqual(first_k_binary(1), ["0"])

    def test_k_zero(self):
        self.assertEqual(first_k_binary(0), [])

    def test_k_three(self):
        self.assertEqual(first_k_binary(3), ["0","1","10"])


if __name__ == "__main__":
    unittest.main()

#Time-taken : 30 minutes