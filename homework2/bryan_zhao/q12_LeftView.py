# Technique: Level-order traversal because the question asks for each level of the tree
# Time Complexity: O(n) because every node needs to be visited.
# Space Complexity: O(w) where w is the width of the tree.

from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def LeftView(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            
            if i == 0:
                result.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    
    return result 

def TestCase():
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    
    root.right.left = Node(9)
    root.right.right = Node(13)
    
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    
    root.right.right.left.right = Node(15) 

    print(LeftView(root))

TestCase()

# Time Spent: 11 minutes