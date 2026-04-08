#Left View
#Time complexity: O(2n) where n is the length of the list as every node is enqueued and dequeued once.
#Taking out the constant, it becomes O(n)
#Space Complexity: O(n/2) + O(h) where n is the number of nodes in the tree (last level is the largest and it can hold roughly n/2 nodes) and h is the height of the tree =.
#After Simplifciation it becomes O(n)
#Technique: Level-Order (Breadth-First) Traversal
#Time Spent: 22 minutes

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LeftView(root):
    res = []

    if not root:
        return res
    
    queue = deque([root])

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()

            if i == 0:
                res.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return res


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
