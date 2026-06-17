from collections import deque

# Data Structure: Queue
# Algorithm: Breadth-First Search
# Time Complexity: O(k)
# Space Complexity: O(k)
# Problem: Given a number k, return an array of the first k binary numbers represented as strings.


def firstKBinaryNumbers(k):
    if k == 0:
        return []
    result = ["0"]
    queue = deque(["1"])
    while len(result) < k:
        s = queue.popleft()
        result.append(s)
        if len(result) < k:
            queue.append(s + "0")
            queue.append(s + "1")
    return result


# Testing
print(firstKBinaryNumbers(5))    # ['0','1','10','11','100']
# ['0','1','10','11','100','101','110','111','1000','1001']
print(firstKBinaryNumbers(10))

# Time: 20 min
