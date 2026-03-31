# Technique: Search binary search tree (BST)
# Time Complexity: O(log n) average, O(n) worst (unbalanced tree)
# Space Complexity: O(1) iterative – no recursion stack needed
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def floor_in_bst(root, target):
    floor = None
    current = root
 
    while current is not None:
        if current.data == target:
            return current.data
        elif current.data > target:
            current = current.left
        else:                 
            floor = current.data    
            current = current.right  
 
    return floor

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)
    return root
 
 
def build_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


bst = build_bst([10, 8, 16, 9, 13, 17, 20])
 
print(floor_in_bst(bst, 13))  
print(floor_in_bst(bst, 15))   
print(floor_in_bst(bst, 25))  
print(floor_in_bst(bst, 5))  
print(floor_in_bst(bst, 8))    
print(floor_in_bst(bst, 20))  
print(floor_in_bst(None, 10))  