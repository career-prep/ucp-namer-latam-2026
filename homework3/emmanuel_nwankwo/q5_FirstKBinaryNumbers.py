# Data Structure: Queue
# Algorithm: Breadth-first search
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

def first_k_binay_numbers(n):
    if n == 0:
        return []
    queue = deque()
    queue.append("1")
    results = ["0"]

    for i in range(n - 1):
        current_bin = queue.popleft()
        results.append(current_bin)
        queue.append(current_bin + "0")
        queue.append(current_bin + "1")

    return results

#Time Taken: 11mins

# Test cases:
print(first_k_binay_numbers(5))
print(first_k_binay_numbers(10))

# Edge Cases:
print(first_k_binay_numbers(1))
print(first_k_binay_numbers(0))
print(first_k_binay_numbers(2))