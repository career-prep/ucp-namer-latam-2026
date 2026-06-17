'''
Method: DFS
Time: 15 mins
Time Complexity: O(n)
Space Complexity: O(h)

Intuition: 
A tree is a BST if every node is within a certain range. 
The left node must be between the root node and the next left node
The right node must be between the root node and the next right node.
If a node violates this, it's not a BST
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def Is_BST(root, low = float('-inf'), high = float('inf')):
    if not root:
        return True
    
    if not (low < root.data < high):
        return False
    return Is_BST(root.left, low, root.data) and Is_BST(root.right, root.data, high)

# Example 1 (expected True)
root1 = Node(10)
root1.left = Node(8)
root1.left.right = Node(9)
root1.right = Node(16)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

# Example 2 (expected False)
root2 = Node(10)
root2.left = Node(8)
root2.left.right = Node(9)
root2.right = Node(16)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)


print(Is_BST(root1))
print(Is_BST(root2))
