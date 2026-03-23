# Technique: Depth-first traversal (pre-order)
# time complexity: O(n)
# space complexity: O(n)
# 10 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
    new_node = Node(root.data)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    return new_node

# helpers for testing
def trees_equal(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.data == b.data and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)

# test cases

# tree: 10 -> (8, 16) -> (9, 13, 17) -> (20)
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

copy = copyTree(root)
assert trees_equal(root, copy)
assert copy is not root
assert copy.left is not root.left
assert copy.right.left is not root.right.left

# empty tree
assert copyTree(None) is None

# single node
single = Node(5)
single_copy = copyTree(single)
assert single_copy.data == 5
assert single_copy is not single
assert single_copy.left is None
assert single_copy.right is None

print("yay!!")
