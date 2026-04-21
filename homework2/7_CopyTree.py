# Technique: Depth-first traversal (pre-order)
# Time: O(n)
# Space: O(n)
# Time Spent: 20 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
                                              
    new_root = Node(root.data)
    new_root.left = copyTree(root.left)
    new_root.right = copyTree(root.right)

    return new_root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

copied = copyTree(root)

inorder(root)
print()
inorder(copied)