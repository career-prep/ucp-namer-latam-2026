#Copy Tree
#Time Complexity = O(n) where n is the number of nodes
#Space Complexity = O(1)
#Depth First - Pre-Order Traversal 
#Time Spent: 5 mins

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
    curr = Node(root.data)
    curr.left = copyTree(root.left)
    curr.right = copyTree(root.right)

    return curr


def print_tree(root):
    if not root:
        return
    print(root.data, end=" ")
    print_tree(root.left)
    print_tree(root.right)


#       10
#      /  \
#     8    16
#      \  / \
#       9 13  17
#               \
#               20

# Test Case 1
root1 = Node(10)
root1.left = Node(8)
root1.left.right = Node(9)
root1.right = Node(16)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

copy1 = copyTree(root1)
print_tree(root1)  
print()
print_tree(copy1) #Printing the preorder traversal is the same as the original preorder traversal
print("\n\n")
#       7
#      / \
#    20   4
#   / \  / \
#  15  6 8  11

# Test Case 2
root2 = Node(7)
root2.left = Node(20)
root2.left.left = Node(15)
root2.left.right = Node(6)
root2.right = Node(4)
root2.right.left = Node(8)
root2.right.right = Node(11)

copy2 = copyTree(root2)
print_tree(root2)
print()
print_tree(copy2)