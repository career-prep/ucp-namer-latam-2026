# Data Structure: Queue
# Technique: BFS-style generation — enqueue "0" and "1", then for each
#             dequeued string append "0" and "1" to get next binary numbers
# Time Complexity: O(k)
# Space Complexity: O(k)

from collections import deque

def firstKBinaryNumbers(k):
    result = []
    queue = deque(["0", "1"])

    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)
        # only expand non-zero to avoid leading zeros past "0" itself
        if curr != "0":
            queue.append(curr + "0")
            queue.append(curr + "1")

    return result


# Test 1: k = 5 -> ["0","1","10","11","100"]
print(firstKBinaryNumbers(5))   # ["0", "1", "10", "11", "100"]

# Test 2: k = 10 -> ["0","1","10","11","100","101","110","111","1000","1001"]
print(firstKBinaryNumbers(10))  # ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]

# Test 3: k = 1 -> ["0"]
print(firstKBinaryNumbers(1))   # ["0"]

# Test 4: k = 2 -> ["0", "1"]
print(firstKBinaryNumbers(2))   # ["0", "1"]

# Test 5: k = 7
print(firstKBinaryNumbers(7))   # ["0", "1", "10", "11", "100", "101", "110"]

# Time spent: ~25 minutes