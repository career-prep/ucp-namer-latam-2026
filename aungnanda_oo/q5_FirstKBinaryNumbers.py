# Question 5: FirstKBinaryNumbers

# Data Structure: Queue
# Generate binary numbers in order by treating each number as a prefix:
# dequeue "x", enqueue "x0" and "x1". Start with "1" after seeding "0".
# Time Complexity: O(k)
# Space Complexity: O(k)

from collections import deque


def firstKBinaryNumbers(k):
    if k == 0:
        return []
    result = ["0"]
    queue = deque(["1"])
    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)
        queue.append(curr + "0")
        queue.append(curr + "1")
    return result


# --- Tests ---

print("k=5:", firstKBinaryNumbers(5))
# ["0", "1", "10", "11", "100"]

print("k=10:", firstKBinaryNumbers(10))
# ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]

print("k=1:", firstKBinaryNumbers(1))   # ["0"]
print("k=0:", firstKBinaryNumbers(0))   # []
print("k=2:", firstKBinaryNumbers(2))   # ["0", "1"]

# Spent a total of 20 mins on this question
