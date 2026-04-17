# Time: O(n) - have to check every node
# Space: O(h) - recursion stack, h = height of tree
 
# CANT just check if left < root < right at each node
# that would miss cases like having a node in the left subtree that's bigger than
# the root of a grandparent instead we pass down valid min/max bounds as we recurse
# every node must be within the range (min_val, max_val)
 
def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    # empty tree is a valid BST
    if root is None:
        return True
 
    # current node must be strictly within bounds
    if root.data <= min_val or root.data >= max_val:
        return False
 
    # when we go left, the current node becomes the new upper bound
    # when we go right, the current node becomes the new lower bound
    return (isBST(root.left, min_val, root.data) and
            isBST(root.right, root.data, max_val))
 
