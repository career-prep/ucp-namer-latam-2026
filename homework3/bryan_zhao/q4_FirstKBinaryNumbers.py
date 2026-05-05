# Data Structure: Queue
# Time Complexity: O(k) since each number is generated exactly once
# Space Complexity: O(k) to store result list and the queue

from collections import deque

def first_k_binary_numbers(k):
    if k <= 0:
        return []
    
    result = ["0"]
    if k == 1:
        return result
    
    queue = deque(["1"])

    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)

        queue.append(curr + "0")
        queue.append(curr + "1")

    return result

print(first_k_binary_numbers(5))
print(first_k_binary_numbers(10))

# Time Spent: 20 min