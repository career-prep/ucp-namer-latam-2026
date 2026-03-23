'''
Method: Level Order
Time: 40 min
Time Complexity: O(n)
Space Complexity: O(n)

Intuition: Look at each level of the tree. 
Use a queue to add all the elements in the level starting from the left most.
Append the first element in the queue to the arr (will be the left most item).

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def LeftView(root):
    arr = []
    if root is None:
        return arr
    queue = [root]
    
    while queue:
        level = len(queue)
        nodes = []

        for i in range(level):
            node = queue.pop(0)
            nodes.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        arr.append(nodes[0])
    return arr


# Test Case 1
#         7
#        / \
#       8   3
#          / \
#         9  13
#        / \
#       20  14
#             \
#             15

root1 = Node(7)
root1.left = Node(8)

root1.right = Node(3)
root1.right.left = Node(9)
root1.right.right = Node(13)

root1.right.left.left = Node(20)
root1.right.left.right = Node(14)
root1.right.left.right.right = Node(15)

#Test Case 2

#       7
#      / \
#    20   4
#   / \ / \
#  15 6  8  11

root2 = Node(7)
root2.left = Node(20)
root2.left.left = Node(15)
root2.left.right = Node(6)

root2.right = Node(4)
root2.right.left = Node(8)
root2.right.right = Node(11)

print(LeftView(root1))
print(LeftView(root2))