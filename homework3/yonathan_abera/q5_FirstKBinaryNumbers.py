# Data Structure: Queue
# Time Complexity: O(k)
# Space Complexity: O(k)

from collections import deque

def firstKBinaryNumbers(k):
    result = []
    queue = deque(["0"])

    for x in range(k):
        curr = queue.popleft()
        result.append(curr)
        if curr == "0":
            queue.append("1")
        else:
            queue.append(curr + "0")
            queue.append(curr + "1")

    return result

print(firstKBinaryNumbers(5))
print(firstKBinaryNumbers(10))

# Time spent: 15 minutes
