class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def isBST(root):
            if root is None:
                return True
            if root.left and root.val < root.left.val:
                return False
            if root.right and root.val > root.right.val:
                return False
            return isBST(root.left) or isBST(root.right)

        return isBST(root)
