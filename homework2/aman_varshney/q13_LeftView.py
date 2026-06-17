# spent 25 minutes
# Time complexity - O(n) 
# Space complexity - O(1)
# BFS

from collections import deque


class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right
        
    
def leftView(tree):
    if not tree: # empty case
        return []
    
    q = deque()
    q.append(tree)
    result = []
    
    while q:
        nodes = len(q) 
        for i in range(nodes):
            node = q.popleft()
            if i == 0: # first in level -> leftmost
                result.append(node.data)
                
            # enqueue children
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
    return result
    
    
    
if __name__ == "__main__":
    root1 = Node(7)
    root1.left = Node(8)
    root1.right = Node(3)
    root1.right.left = Node(9)
    root1.right.right = Node(13)
    root1.right.left.left = Node(20)
    root1.right.right.left = Node(13)
    root1.right.right.left = Node(14)
    root1.right.right.left.right = Node(15)
    print("Test 1")
    l1 = leftView(root1) 
    print("Actual: ", l1)
    print("Expected: [7, 8, 9, 20, 15]")
    
    print()
    
    root2 = Node(7)
    root2.left = Node(20)
    root2.right = Node(4)
    root2.left.left = Node(15)
    root2.left.right = Node(6)
    root2.right.left = Node(8)
    root2.right.right = Node(11)
    print("Test 2")
    l2 = leftView(root2) 
    print("Actual: ", l2)
    print("Expected: [7, 20, 15]")