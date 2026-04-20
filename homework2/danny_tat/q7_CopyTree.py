# Question 7: Copy Tree
# Technique: Depth-first traversal (Pre-order)
# Time: O(n)
# Space: O(n) — recursion stack + new tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def CopyTree(root):
    if not root:
        return None
    new_node = Node(root.data)
    new_node.left = CopyTree(root.left)
    new_node.right = CopyTree(root.right)
    return new_node

# time: 15 minutes
