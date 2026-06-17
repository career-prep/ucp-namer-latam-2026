"""
Technique: Search binary search tree (BST)
Time Complexity: O(h) - Average O(log n), worst case O(n) if skewed.
Space Complexity: O(1) - Iterative approach uses no extra space.
"""

from xml.dom import Node


def floor_in_bst(root, target):
    floor = None
    curr = root
    while curr:
        if curr.val == target:
            return curr.val # Exact match is the best possible floor
        if curr.val > target:
            curr = curr.left
        else:
            floor = curr.val
            curr = curr.right
    return floor

# --- Test Cases ---
if __name__ == "__main__":
    # BST:     10
    #        /    \
    #       5      15
    #             /  \
    #            12   20
    bst_root = Node(10, Node(5), Node(15, Node(12), Node(20)))
    print(f"Floor of 13: {floor_in_bst(bst_root, 13)}") # Expected: 12
    print(f"Floor of 15: {floor_in_bst(bst_root, 15)}") # Expected: 15