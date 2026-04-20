# Technique: Simultaneous iteration two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def IsBST(self):
        
        def IsBST_helper(root, min_val, max_val):
            if root is None:
                return True
            
            if not (min_val < root.data < max_val):
                return False
            
            return (IsBST_helper(root.left, min_val, root.data) and 
                    IsBST_helper(root.right, root.data, max_val))
        
        return IsBST_helper(self, float('-inf'), float('inf'))


# (valid BST)

# root = TreeNode(10)
# root.left = TreeNode(8)
# root.right = TreeNode(16)
# root.left.right = TreeNode(9)
# root.right.left = TreeNode(13)

# print(root.IsBST())  # True


#(invalid BST)

# root2 = TreeNode(10)
# root2.left = TreeNode(5)
# root2.right = TreeNode(15)
# root2.right.left = TreeNode(6)  # ❌ invalid

# print(root2.IsBST())  # False