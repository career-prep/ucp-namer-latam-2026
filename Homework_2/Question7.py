# Given a binary tree, create a deep copy. Return the root of the new tree.

# Technique: Depth-first traversal (generic)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def copy_tree(root):
    if root is None:
        return None
    new_node = Node(root.data)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)
    return new_node


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
copy = copy_tree(root)
print(inorder(copy))
copy.left.data = 99
print(inorder(root))
print(inorder(copy))
print(copy_tree(None))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Spent 20 mins
