#Time: O(n)
#Space: O(h)

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root) -> bool:
    def is_valid(node, minn, maxx):
        if not node:
            return True
        
        if node.val <= minn or node.val >= maxx:
            return False
        
        return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

    return is_valid(root, float("-inf"), float("inf"))

#Time-taken: 20 minutes

class TestIsValidBST(unittest.TestCase):

    def test_empty_tree(self):
        root = None
        self.assertTrue(isValidBST(root))

    def test_single_node(self):
        root = TreeNode(10)
        self.assertTrue(isValidBST(root))

    def test_valid_bst(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(20)

        self.assertTrue(isValidBST(root))

    def test_invalid_bst_local_violation(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(8)

        self.assertFalse(isValidBST(root))

    def test_invalid_bst_global_violation(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)

        self.assertFalse(isValidBST(root))

    def test_duplicates_not_allowed(self):
        root = TreeNode(10)
        root.left = TreeNode(10)

        self.assertFalse(isValidBST(root))


if __name__ == "__main__":
    unittest.main()