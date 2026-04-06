# Technique: Tree Traversal - Depth-first (Post-order)
# Time Complexity: O(n)
# Space Complexity: O(h)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
 
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root

def copyTree(root):
    if root is None:
        return None

    new_left = copyTree(root.left)
    new_right = copyTree(root.right)

    new_node = Node(root.val)
    new_node.left = new_left
    new_node.right = new_right

    return new_node


values = [5, 3, 7, 2, 4, 6, 8]
original_root = None
for v in values:
    original_root = insert(original_root, v)

copied_root = copyTree(original_root)

print(f"Original root value: {original_root.val}")
print(f"Copied root value:   {copied_root.val}")

if original_root is not copied_root:
    print("Success: These are two different trees in memory.")

# Time Spent: 15 minutes