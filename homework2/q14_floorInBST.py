# Search Binary Search Tree (BST)
# O(log(n)) Time Complexity (Assuming BST is balanced... But, O(n) in the worst case if not balanced)
# O(1) Space Complexity
# Given a target numeric value and a BST, return the floor (the greatest value less than or equal to the target) in the BST

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def floorInBST(root, target):

    if root == None:
        return None
    
    if root.data == target:
        return target
    

    # Store our best result currently, update this as we search the BST
    currRes = float("-inf")

    while root:

        if root.data == target:
            return target
        
        elif root.data > target:
            
            # We know root.data > target, so it cannot be the floor. No need to update currRes

            # Search left
            root = root.left

        else:
            # root.data < target

            if root.data > currRes: # We also know root.data < target
                currRes = root.data

            # Search right
            root = root.right



    if currRes != float("-inf"):
        return currRes
    else:
        return None
            


# 22 minutes


# Test Cases

# BST 1
root1 = TreeNode(10)
root1.left = TreeNode(8)
root1.left.right = TreeNode(9)
root1.right = TreeNode(16)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(17)
root1.right.right.right = TreeNode(20)


print(floorInBST(root1, 13))
print(floorInBST(root1, 15))