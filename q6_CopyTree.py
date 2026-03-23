#Time: O(n)
#Space: O(h)

class TreeNode:
    def _init_(self, val=0, left=None, right=None):
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
