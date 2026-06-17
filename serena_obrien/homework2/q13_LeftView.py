# Time complexity: O(n)
# Space complexity: O(n)

# Technique: Level-order (breadth-first) traversal

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == 0:
                result.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return result

if __name__ == '__main__':
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(13)
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    root.right.right.left.right = Node(15)

    lv = leftView(root)
    print("Left view of the binary tree:", lv)

# ~ time spent: 35 minutes