#Time Complexity: O(h))
#Space Complexity: O(h)
#Technique: Search BST

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def floorInBst(root, target):

    def helper(root, best):
        if not root:
            return best
        
        if target > root.val:
            best = root.val
            return helper(root.right, best)

        elif target < root.val:
            return helper(root.left, best)

        elif target == root.val:
            return target
    
    return helper(root, None)

root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(10)

print(floorInBst(root, 10))
print(floorInBst(root, 5)) 
print(floorInBst(root, 2)) 


#Time taken 25 min