# Given a binary tree, create an array of the left view (leftmost
# elements in each level) of the tree.

# Examples:

# Input:           7
#               /     \
#             8         3
#            / \       / \
#           9   13   20   4
#          /          \
#        20            18
#        /
#      15
# Output: [7, 8, 9, 20, 15]

# Input:       7
#            /   \
#          20     3
#         /
#        15
# Output: [7, 20, 15]

# Technique: Level-order (breadth-first) traversal

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


root = Node(7)
root.left = Node(8)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(13)
root.right.left = Node(20)
root.right.right = Node(4)
root.left.left.left = Node(20)
root.right.left.right = Node(18)
root.left.left.left.left = Node(15)
print(left_view(root))

root2 = Node(7)
root2.left = Node(20)
root2.right = Node(3)
root2.left.left = Node(15)
print(left_view(root2))

print(left_view(None))

root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
print(left_view(root3))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Spent 30 mins
