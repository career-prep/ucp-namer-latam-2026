class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBST(root):
    def check(node, low, high):
        if not node:
            return True
        if (low != None and node.val <= low) or (high != None and node.val >= high):
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, None, None)
# time: O(n)
