#Technique: DFS generic 
#Time Complexit O(n)
#Space Complexity O(h) where h is tree height

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
    
    newNode = TreeNode(root.data)
    
    newNode.left = copyTree(root.left)
    newNode.right = copyTree(root.right)

    return newNode

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

copy = copyTree(root)
inorder(root)

#Time taken 18 min

