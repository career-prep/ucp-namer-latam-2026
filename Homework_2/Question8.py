# Given a binary tree, determine if it is a binary search tree.

# Examples:

# Input:       10
#            /    \
#          5       15
#         / \     /  \
#        3   7  12    18
# Output: True

# Input:       10
#            /    \
#          5       15
#         / \
#        3   12
# Output: False

# Technique: Depth-first traversal (in-order)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root):
    values = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        values.append(node.data)
        inorder(node.right)
    inorder(root)
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False
    return True


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)
print(is_bst(root))

root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.left.left = Node(3)
root2.left.right = Node(12)
print(is_bst(root2))

print(is_bst(None))

root3 = Node(5)
root3.left = Node(5)
print(is_bst(root3))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Spent 25 mins
