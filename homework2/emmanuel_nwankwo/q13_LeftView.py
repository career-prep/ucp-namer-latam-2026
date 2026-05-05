# Technique: Level-order (breadth-first) traversal
# Time Complexity: O(n)
# Space Complexity: O(w) where w is max width of the tree

from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def left_view(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0: result.append(node.data)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return result

# Time Taken: 10mins 32secs
# Testcases
t1 = Node(7)
t1.left = Node(8)
t1.right = Node(3)
t1.right.left = Node(9)
t1.right.right = Node(13)
t1.right.left.left = Node(20)
t1.right.right.left = Node(14)
t1.right.right.left.right = Node(15)

print(left_view(t1))

t2 = Node(7)
t2.left = Node(20)
t2.right = Node(4)
t2.left.left = Node(15)
t2.left.right = Node(6)
t2.right.left = Node(8)
t2.right.right = Node(11)

print(left_view(t2))

# Edge cases
t3 = None
print(left_view(t3))

t4 = Node(42)
print(left_view(t4))