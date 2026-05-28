# First K Binary Numbers
# Data Structure: Queue
# Time Complexity: O(K) where K is the number of binary numbers to generate
# Space Complexity: O(K) where K is the size of the result array and queue combined

from collections import deque

def firstKBinaryNumbers(k):
    if k == 0:
        return []
    

    list_of_binary_strings = ["0"]
    bfs_queue = deque(["1"])

    while len(list_of_binary_strings) < k:
        current_binary_string = bfs_queue.popleft()
        list_of_binary_strings.append(current_binary_string)
        
        if len(list_of_binary_strings) < k:
            bfs_queue.append(current_binary_string + "0")
            bfs_queue.append(current_binary_string + "1")
        
    return list_of_binary_strings

#Test Cases
print(firstKBinaryNumbers(5))   # expected: ["0", "1", "10", "11", "100"]
print(firstKBinaryNumbers(10))  # expected: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
print(firstKBinaryNumbers(1))   # expected: ["0"]
print(firstKBinaryNumbers(0))   # expected: []