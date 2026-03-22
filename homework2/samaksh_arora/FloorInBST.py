#Floor In BST
#Time Complexity: O(h) where h is the height of the tree
#Space Complexity: O(1)
#Technique: Search Binary Search Tree (BST)
#Time Taken: 35min

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def FloorInBST(root, target):
    floor = None
    curr = root

    while curr:
        if curr.data == target:
            return curr.data
        elif curr.data > target:
            curr = curr.left
        else:
            floor = curr.data
            curr = curr.right

    return floor


#Test cases

root = Node(10)
root.left = Node(8)
root.left.right = Node(9)

root.right = Node(16)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)


target = 13
target2 = 15

print(FloorInBST(root, target))
print(FloorInBST(root, target2))
