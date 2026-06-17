# Technique: Depth-first traversal (Pre-order)
# Time Complexity: O(n)
# Space Complexity: O(h)

def is_bst(root):
    def recurseTree(node, min_val, max_val):
        if node is None:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False

        return recurseTree(node.left, min_val, node.data) and recurseTree(node.right, node.data, max_val)

    return recurseTree(root, float("-inf"), float("inf"))

# Time Taken: 7mins 4secs

# Test Cases
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = Node(10)
tree1.left = Node(8)
tree1.right = Node(16)
tree1.left.right = Node(9)
tree1.right.left = Node(13)
tree1.right.right = Node(17)
tree1.right.right.right = Node(20)

print(is_bst(tree1))

tree2 = Node(10)
tree2.left = Node(8)
tree2.right = Node(16)
tree2.left.right = Node(9)
tree2.right.left = Node(13)
tree2.right.right = Node(17)
tree2.right.right.right = Node(15)

print(is_bst(tree2))

# Edge Cases
tree3 = None
print(is_bst(tree3))

tree4 = Node(42)
print(is_bst(tree4))

tree5 = Node(10)
tree5.left = Node(10)
print(is_bst(tree5))