# Technique: search binary search tree
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Time spent: 23 minutes
 
from q3_binarySearchTree import Node
 
 
def floor_in_bst(root, target):
    floor_val = None
    curr = root

    while curr:
        if curr.data == target:
            return curr.data
        elif curr.data < target:
            floor_val = curr.data
            curr = curr.right
        else:
            curr = curr.left
    
    return floor_val
 
 
def build_tree(val, left=None, right=None):
    node = Node(val)
    node.left = left
    node.right = right
    return node
 

bst = build_tree(10, build_tree(8, None, build_tree(9)), build_tree(16, build_tree(13), build_tree(17, None, build_tree(20))))
 

print(floor_in_bst(bst, 13))  # expected 13
print(floor_in_bst(bst, 15))  # expected 13