class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isBST(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True

    if node.val <= low or node.val >= high:
        return False

    return isBST(node.left, low, node.val) and isBST(node.right, node.val, high)


def insert(root, val):
    if not root: 
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else: 
        root.right = insert(root.right, val)
    return root


root1 = None
for v in [10, 5, 15]:
    root1 = insert(root1, v)
print(f"Test 1 (Valid): {isBSTIterative(root1)}") 


root2 = Node(10)
root2.left = Node(5)
root2.right = Node(8)
print(f"Test 2 (Invalid): {isBSTIterative(root2)}")


# Technique: Tree Traversal - Depth-first (Recursive with Range)
# Time Complexity: O(n) 
# Space Complexity: O(h) 
# Time Spent: 25 minutes
