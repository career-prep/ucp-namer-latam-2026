# Technique: Depth-first traversal (generic) with valid range tracking
# time complexity: O(n)
# space complexity: O(n) for recursion stack
# 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    def helper(node, min_val, max_val):
        if not node:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return (helper(node.left, min_val, node.data) and
                helper(node.right, node.data, max_val))
    return helper(root, float('-inf'), float('inf'))

# test cases

# valid BST: 10 -> (8, 16) -> (9, 13, 17) -> (20)
root1 = Node(10)
root1.left = Node(8)
root1.right = Node(16)
root1.left.right = Node(9)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)
assert isBST(root1) == True

# invalid BST: 15 is right child of 17, but 15 < 17 (violates BST property from ancestor)
root2 = Node(10)
root2.left = Node(8)
root2.right = Node(16)
root2.left.right = Node(9)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)
assert isBST(root2) == False

# single node
assert isBST(Node(42)) == True

# empty tree
assert isBST(None) == True

# invalid: left child greater than root
root3 = Node(5)
root3.left = Node(7)
assert isBST(root3) == False

print("yay!!")
