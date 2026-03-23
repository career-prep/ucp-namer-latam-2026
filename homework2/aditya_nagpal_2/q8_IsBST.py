# Approach:
# We use recursion with range limits.
# Each node must lie within a valid range (low, high).
# For left subtree → values must be < current node
# For right subtree → values must be > current node
# We keep updating the range as we go down the tree.

# considered that the height is within limits of BST
# Time Complexity: O(n)
# → We visit each node exactly once

# Space Complexity: O(h)

# → Worst case: O(n), Best case (balanced): O(log n)

def isBST(root):
    def helper(node, low, high):
        if not node:
            return True
        
        # Check if current node violates BST property
        if not (low < node.data < high):
            return False
        
        # Recurse left and right with updated bounds
        return helper(node.left, low, node.data) and helper(node.right, node.data, high)
    
    return helper(root, float('-inf'), float('inf'))