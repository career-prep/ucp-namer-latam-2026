# Technique: depth-first traversal - pre-order
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 10 minutes
 
from q3_binarySearchTree import Node
 
 
def copy_tree(root):
    if root is None:
        return None
    
    new_root = Node(root.data)
    new_root.left = copy_tree(root.left)
    new_root.right = copy_tree(root.right)
    return new_root
    
 
 
 
def build_tree(val, left=None, right=None):
    node = Node(val)
    node.left = left
    node.right = right
    return node
 
 
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)

original = build_tree(10, build_tree(8, None, build_tree(9)), build_tree(16, build_tree(13), build_tree(17, None, build_tree(20))))
copy = copy_tree(original)
print(inorder(copy))        #expected [8, 9, 10, 13, 16, 17, 20]
print(original is not copy) # expected True 

copy = copy_tree(None)
print(copy)                 # expected None

copy = copy_tree(build_tree(42))
print(inorder(copy))        # expected [42]

copy = copy_tree(build_tree(1, build_tree(2, build_tree(3), None), None))
print(inorder(copy))        #expected [3, 2, 1]

copy = copy_tree(build_tree(1, build_tree(2, build_tree(4), build_tree(5)), build_tree(3, build_tree(6), build_tree(7))))
print(inorder(copy))        # expected [4, 2, 5, 1, 6, 3, 7]