#Time: O(n)
#Space: O(h)

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def copyTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    new_node = TreeNode(root.val)
    
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    
    return new_node

#Time-taken: 30 minutes
class TestCopyTree(unittest.TestCase):

    def compareTrees(self, t1, t2):
        """Helper function to check if two trees are identical in structure and value"""
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val and
            self.compareTrees(t1.left, t2.left) and
            self.compareTrees(t1.right, t2.right)
        )

    def test_empty_tree(self):
        root = None
        copied = copyTree(root)
        self.assertIsNone(copied)

    def test_single_node(self):
        root = TreeNode(1)
        copied = copyTree(root)

        self.assertIsNot(root, copied)  
        self.assertEqual(root.val, copied.val)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        copied = copyTree(root)

        self.assertTrue(self.compareTrees(root, copied))
        self.assertIsNot(root, copied)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        copied = copyTree(root)

        self.assertTrue(self.compareTrees(root, copied))

    def test_deep_copy_independence(self):
        root = TreeNode(1)
        root.left = TreeNode(2)

        copied = copyTree(root)

        root.left.val = 99

        self.assertNotEqual(root.left.val, copied.left.val)


if __name__ == "__main__":
    unittest.main()