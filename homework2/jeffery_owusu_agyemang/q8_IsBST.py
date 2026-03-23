"""
Technique: Search Binary Search Tree (BST)
Time Complexity: O(n) - Every node is checked once.
Space Complexity: O(h) -stack depth based on tree height.
Time spent: 37 minutes
"""

def is_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
    return validate(root, float('-inf'), float('inf'))    # Starting with widest possible range 

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Valid BST
    #      5
    #     / \
    #    3   7
    valid_tree = Node(5, Node(3), Node(7))
    print(f"Test 1 (Valid): {is_bst(valid_tree)}") # Expected: True

    # Test 2: Invalid BST (7 is to the left of 5)
    #      5
    #     / \
    #    7   3
    invalid_tree = Node(5, Node(7), Node(3))
    print(f"Test 2 (Invalid): {is_bst(invalid_tree)}") # Expected: False