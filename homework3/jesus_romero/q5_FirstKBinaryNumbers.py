# Technique: Queue-based level-order generation (BFS for binary strings)

from collections import deque

def firstKBinaryNumbers(k): # Time Complexity: O(k), Space Complexity: O(k)
    # 1. Handle edge case for k=0
    if k <= 0:
        return []
    
    # 2. Use a queue to generate binary numbers in order
    # Start with "0" if k >= 1 (per example, 0 is the first number)
    result = []
    queue = deque(["1"])
    
    # Per example, the first number is "0"
    result.append("0")
    if k == 1:
        return result

    # 3. BFS-like generation: append '0' then '1' to current string to get next level
    while len(result) < k:
        curr = queue.popleft()
        result.append(curr)
        
        # Check if we still need more numbers before adding to queue
        if len(result) + len(queue) < k * 2: # Optimization to stop early
            queue.append(curr + "0")
            queue.append(curr + "1")
            
    return result[:k]

class Test:
    def run_tests(self):
        # 1. Test Case: k = 5
        # Expected: ["0", "1", "10", "11", "100"]
        assert firstKBinaryNumbers(5) == ["0", "1", "10", "11", "100"]
        
        # 2. Test Case: k = 10
        # Expected: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
        assert firstKBinaryNumbers(10) == ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
        
        # 3. Test Case: k = 1
        assert firstKBinaryNumbers(1) == ["0"]

        print("FirstKBinaryNumbers tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()

# Time complexity: O(k) - each number is generated and appended once.
# Space complexity: O(k) - to store the result array and the queue.