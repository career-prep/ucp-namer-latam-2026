class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def copyTree(root):
    if not root:
        return None
    new_root = Node(root.val)
    new_root.left = copyTree(root.left)
    new_root.right = copyTree(root.right)
    return new_root
# time: O(n)