# Algorithm: BFS-style generation (each popped string seeds two children: s+"0" and s+"1")
# Time Complexity: O(k * log k) — each of the k strings has length up to log k
# Space Complexity: O(k * log k)

from collections import deque


def firstKBinaryNumbers(k):
    if k <= 0:
        return []
    result = ["0"]
    if k == 1:
        return result
    queue = deque(["1"])
    while len(result) < k:
        s = queue.popleft()
        result.append(s)
        if len(result) < k:
            queue.append(s + "0")
            queue.append(s + "1")
    return result


print("FirstKBinaryNumbers Results:")

print(firstKBinaryNumbers(5))
print(firstKBinaryNumbers(10))
print(firstKBinaryNumbers(1))
print(firstKBinaryNumbers(0))
print(firstKBinaryNumbers(16))
