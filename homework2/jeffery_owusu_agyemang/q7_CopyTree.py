"""
Technique: Tree Traversal - Pre-order traversal
Time Complexity: O(n) - We visit every node exactly once.
Space Complexity: O(h) - Where h is the height of the tree, representing the recursion stack.
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def copy_tree(root):
    if not root:
        return None
    new_node = Node(root.val)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)
    
    return new_node

# --- Test Cases ---
if __name__ == "__main__":
    # Constructing:     1
    #                 /   \
    #                2     3
    original = Node(1, Node(2), Node(3))
    cloned = copy_tree(original)
    
    print(f"Original Root: {original.val}, Cloned Root: {cloned.val}")
    print(f"Are they the same object? {original == cloned}") # expected False
    print(f"Are the left children same value? {original.left.val == cloned.left.val}") # expected True