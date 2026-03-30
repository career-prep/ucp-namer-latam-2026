#Time: O(n)
#Space: O(n)

from collections import deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftview(root):
    if not root:
        return []
    
    queue = deque()
    
    res = []
    queue.append(root)
    

    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.popleft()

            if i == 0:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res

#Time-taken: 15 minutes


class TestLeftView(unittest.TestCase):

    def test_balanced_tree(self):
        root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(leftview(root), [1, 2, 4])

    def test_left_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(leftview(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(leftview(root), [1, 2, 3])

    def test_single_node(self):
        root = TreeNode(10)
        self.assertEqual(leftview(root), [10])

    def test_tree_with_missing_children(self):
        root = TreeNode(1,
                TreeNode(2, None, TreeNode(5, TreeNode(6))))
        self.assertEqual(leftview(root), [1, 2, 5, 6])

    def test_two_levels(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(leftview(root), [1, 2])


if __name__ == "__main__":
    unittest.main()




