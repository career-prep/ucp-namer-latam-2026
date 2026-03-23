#Technique Search BST
#Time Complexity: O(n)
#Space Complexity O(h)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    def checkBST(root, minn, maxx):
        if not root:
            return True
            
        if root.data <= minn or root.data >= maxx:
            return False
            
        return checkBST(root.left, minn, root.data) and checkBST(root.right, root.data, maxx)
        
    return checkBST(root, float('-inf'), float('inf'))
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)

print(isBST(root))

root2 = TreeNode(3)
root2.left = TreeNode(4)

print(isBST(root2))

#Time taken: 20 min
