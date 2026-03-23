# Technique: search BST
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 40 minutes

from q3_binarySearchTree import Node

def is_bst(root):
    def valid(node, left, right):
        if not node:
            return True
        
        if not (node.data < right and node.data > left):
            return False
        
        return (valid(node.left, left, node.data) and valid(node.right, node.data, right))
    return valid(root, float("-inf"), float("inf"))

def build_tree(val, left=None, right=None):
    node = Node(val)
    node.left = left
    node.right = right
    return node

tree1 = build_tree(10, build_tree(8, None, build_tree(9)), build_tree(16, build_tree(13), build_tree(17, None, build_tree(20))))
print(is_bst(tree1))

print(is_bst(None))

tree2 = build_tree(10, build_tree(8, None, build_tree(9)), build_tree(16, build_tree(13), build_tree(17, None, build_tree(15))))
print(is_bst(tree2))  