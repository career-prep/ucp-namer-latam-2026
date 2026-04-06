# Technique: Level-order (breadth-first) traversal
# Time Complexity: O(n) - visit every node once
# Space Complexity: O(w) - queue holds at most one full level (w = max width)
 
from collections import deque
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def left_view(root):
    if root is None:
        return []
 
    result = []
    queue = deque([root])
 
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:               
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
    return result

root1 = Node(7)
root1.left = Node(8)
root1.right = Node(3)
root1.right.left = Node(9)
root1.right.right = Node(13)
root1.right.left.left = Node(20)
root1.right.left.right = Node(14)
root1.right.left.right.right = Node(15)
 
root2 = Node(7)
root2.left = Node(20)
root2.right = Node(4)
root2.left.left = Node(15)
root2.left.right = Node(6)
root2.right.left = Node(8)
root2.right.right = Node(11)
 

root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
 
print(left_view(root1))   
print(left_view(root2))      
print(left_view(root3))    
print(left_view(Node(42)))   
print(left_view(None))   