from collections import deque

def firstKBinary(k):
    if k <= 0:
        return []

    result = []
    queue = deque(["0", "1"])

    for _ in range(k):
        curr = queue.popleft()
        result.append(curr)

        queue.append(curr + "0")
        queue.append(curr + "1")

    return result
    
# 40
