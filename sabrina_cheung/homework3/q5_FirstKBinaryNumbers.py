# Method: BFS
# Space Complexity: O(N)
# Time Complexity: O(N)
# Total Time Taken: 20 mins

from collections import deque

def FirstKBinaryNumbers(num):
    if num <= 0:
        return []
    
    binary = ["0"]
    q = deque(["1"])

    while num > 1:
        cur = q.popleft()
        binary.append(cur)
        q.append(cur + "0")
        q.append(cur + "1")
        num -= 1
    return binary

print(FirstKBinaryNumbers(5))
print(FirstKBinaryNumbers(10))
print(FirstKBinaryNumbers(0))