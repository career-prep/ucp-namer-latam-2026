#isBST
#Time Complexity: O(n) where n is the number of nodes
#Technique: Depth-First Traversal (Generic)
#Time Taken

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def isBST(root,low, high):
    if not root:
        return True
    if root.data <= low or root.data >= high:
        return False
    
    left = isBST(root.left, low, root.data)

    if not left:
        return False
    
    right = isBST(root.right, root.data, high)

    if not right:
        return False

    return True


# Test Case 1
root1 = Node(10)
root1.left = Node(8)
root1.left.right = Node(9)

root1.right = Node(16)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

# Test Case 2
root2 = Node(10)
root2.left = Node(8)
root2.left.right = Node(9)

root2.right = Node(16)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)


low = float('-inf')
high = float('inf')
print(isBST(root1, low, high))
print(isBST(root2, low, high))
