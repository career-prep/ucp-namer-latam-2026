# Runtime: O(klogk)
# Space complexity: O(klogk)
# Data Structure: Tree + Queue
# Algorithm: N/A

import collections
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def firstKBinaryNumbers(target):
    if target <= 0:
        return []
    result = ["0"]
    curr = 1
    source = Node("1")
    q = collections.deque()
    q.append(source)
    while curr < target:
        currNode = q.popleft()
        curr += 1
        result.append(currNode.val)
        currNode.left = Node(currNode.val + "0")
        currNode.right = Node(currNode.val + "1")
        q.append(currNode.left)
        q.append(currNode.right)
    return result

print(firstKBinaryNumbers(5))
print(firstKBinaryNumbers(10))
print(firstKBinaryNumbers(0))
print(firstKBinaryNumbers(-1))
print(firstKBinaryNumbers(1))
print(firstKBinaryNumbers(2))

# Time Spent: 30:00
