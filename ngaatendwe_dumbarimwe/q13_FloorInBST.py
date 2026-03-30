#Time: O(h)
#Space: O(h)

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floorinbst(root,target):
    ans = [float("-inf")]
    
    def helper(root):
        if not root:
            return 
        
        elif target >= root.val:
            ans[0] = max(ans[0], root.val)
            helper(root.right)
        elif target < root.val:
            helper(root.left)
    
    helper(root)
    return ans[0]

#Time-taken: 15 minutes


class TestFloorInBST(unittest.TestCase):

    def test_exact_match(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertEqual(floorinbst(root, 10), 10)

    def test_floor_in_left_subtree(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertEqual(floorinbst(root, 7), 5)

    def test_floor_in_right_subtree(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertEqual(floorinbst(root, 14), 10)

    def test_target_smaller_than_all(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertEqual(floorinbst(root, 2), float("-inf"))

    def test_target_larger_than_all(self):
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertEqual(floorinbst(root, 20), 15)

    def test_single_node(self):
        root = TreeNode(8)
        self.assertEqual(floorinbst(root, 10), 8)

    def test_skewed_tree(self):
        root = TreeNode(5, None,
                TreeNode(10, None,
                TreeNode(15, None,
                TreeNode(20))))
        self.assertEqual(floorinbst(root, 17), 15)


if __name__ == "__main__":
    unittest.main()
