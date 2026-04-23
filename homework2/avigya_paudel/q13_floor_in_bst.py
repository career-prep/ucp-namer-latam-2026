# Technique: Generic Traversal for BST
# Time Complexity: O(log(N))
# Space Complexity: O(log(N))

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node|None = None
        self.right: Node|None = None

def floor_in_bst(root, target):
    # Given a target numeric value and a binary search tree, 
    # return the floor (greatest element less than or equal to the target) in the BST.


    # Note: I chose -1, I did similar for may other edge cases in previous questions,
    # I will ask my interviewer in real interview about what to choose
    if not root: return -1 

    def find_floor(node, target, prev):
        if not node:
            return prev if prev <= target else -1
        
        if node.data == target: return target 

        if node.data > target: 
            return find_floor(node.left, target, prev)
        if node.data < target:
            if node.right: 
                return find_floor(node.right, target, node.data)
            else:
                return prev

    return find_floor(root, target, root.val)