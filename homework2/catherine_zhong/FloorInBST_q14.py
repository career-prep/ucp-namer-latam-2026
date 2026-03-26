#technique: generic search
#time complexity: O(n)
#space complexity: O(1)

class Node:
    def __init__(self,data):
        self.val = data
        self.right = None 
        self.left = None 

def FloorInBST(root, target):
    result = float('-inf')

    current = root
    while current:
        if current.val > result and current.val <= target:
            result = current.val
            current = current.right

        elif current.val > result:
            current = current.left

        else:
            current = current.right

    return result

root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.right.left = Node(13)
root.right.right = Node(17)
root.left.right = Node(9)
root.right.right.right = Node(20)

x = 14
print('test1: ')
print(FloorInBST(root, x))

#time spent: 15min