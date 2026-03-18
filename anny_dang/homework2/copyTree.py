class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def copyTree(root):
    """
    Given a binary tree root, create a deep copy.
    Return the root of the new tree.

    Time: O(n)
    Space: O(h = tree height)
    """
    if not root:
        return None
    
    new_root = Node(root.data)
    new_root.left = copyTree(root.left)
    new_root.right = copyTree(root.right)
    return new_root
