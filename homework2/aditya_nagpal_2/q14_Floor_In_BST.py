# Approach:
# Use BST property to navigate:
# - If node value == target → return it (exact match)
# - If node value > target → go left (smaller values)
# - If node value <= target → it can be a candidate for floor
#     → store it and go right to find a larger valid candidate
#
# Keep updating the best possible floor while traversing.

# Time Complexity: O(h)
# → h = height of tree (O(log n) if balanced, O(n) worst case)

# Space Complexity: O(1)
# → iterative approach

def floorBST(root, target):
    floor_val = None

    while root:
        if root.data == target:
            return root.data
        
        elif root.data > target:
            root = root.left
        
        else:
            floor_val = root.data
            root = root.right

    return floor_val






#given: a bst, target val
#return: GREATEST element  LESS THAN or EQUAL to the TARGET

#compare the element using search in bst

def FloorInBST(root, target):

    if not root: return None
    floor_val = -1

    while root:

        if target == root.data:
            return root.data
        
        if target < root.data:
            root = root.left

        else:
                floor_val = root.data
                root = root.right

         
        return floor_val   #eg target = 10, root.data = 5
    
