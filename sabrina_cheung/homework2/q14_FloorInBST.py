'''
Method: BST Search
Time: 30 Min
Time Complexity: O(n)
Space Complexity: O(1)

Intuition: Since the tree is a binary search tree, we know the tree is sorted.
Go down the tree and if the value is bigger that the current node, move right. If smaller, move left.
If the node is the value being searched, return the node. Otherwise move down until you are unable to move.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def FloorInBST(root, target):
    if root is None:
        return None
    
    if root.data == target:
        return root.data
    
    if root.data < target:
        if root.right:
            return FloorInBST(root.right, target)
        else:
            return root.data
    if root.data > target:
        if root.left:
            return FloorInBST(root.left, target)
        else:
            return root.data
    

#           10
#        /      \
#       8        16
#        \      /    \
#         9  13     17
#                       \
#                         19

root = Node(10)
root.left = Node(8)
root.left.right = Node(9)

root.right = Node(16)
root.right.left = Node(13)
root.right.right = Node(17)

root.right.right.right = Node(19)

# Test Case 1: Target = 13
# Test Case 2: Target = 15

print(FloorInBST(root, 13))
print(FloorInBST(root, 15))