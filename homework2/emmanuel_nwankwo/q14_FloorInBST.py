# Technique: Search binary search tree (BST)
# Time Complexity: O(h)
# Space Complexity: O(1)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def floor_in_bst(root, target):
    floor, curr = None, root
    while curr:
        if curr.data == target: return curr.data
        if curr.data > target: curr = curr.left
        else:
            floor = curr.data
            curr = curr.right
    return floor

# Time Taken: 8mins 54secs
# Testcases
t1 = Node(10)
t1.left = Node(8)
t1.right = Node(16)
t1.left.right = Node(9)
t1.right.left = Node(13)
t1.right.right = Node(17)
t1.right.right.right = Node(20)
print(floor_in_bst(t1, 13))

t2 = Node(10)
t2.left = Node(8)
t2.right = Node(16)
t2.left.right = Node(9)
t2.right.left = Node(13)
t2.right.right = Node(17)
t2.right.right.right = Node(20)
print(floor_in_bst(t2, 15))

# Edge cases
t3 = None
print(floor_in_bst(t3, 10))

t4 = Node(10)
t4.left = Node(5)
t4.right = Node(15)
print(floor_in_bst(t4, 2))