# Data Structure: Queue
# Algorithm: Breadth-First Search (BFS)
# Time Complexity: O(k)
# Space Complexity: O(k)

from collections import deque

def firstKBinaryNumbers(k):
    if k <= 0:
        return []
    
    result = []
    queue = deque(["1"])
    
    if k >= 1:
        result.append("0")
    
    while len(result) < k:
        current = queue.popleft()
        result.append(current)
        
        queue.append(current + "0")
        queue.append(current + "1")
        
    return result[:k]

def main():
    print(f"Test Case 1 (k=5) - Result: {firstKBinaryNumbers(5)}")
    print(f"Test Case 2 (k=10) - Result: {firstKBinaryNumbers(10)}")
    print(f"Test Case 3 (k=1) - Result: {firstKBinaryNumbers(1)}")

if __name__ == "__main__":
    main()

# Time Spent: 29 minutes