# 12 minutes
# Technqiue: Level-order (breadth-first) traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def FloorInBST(head, target):

    current = head
    current_largest = float("-inf")

    while current is not None:
        if current.data < target:
            current_largest = current.data
            current = current.right
            
        elif current.data > target:
            current = current.left

        elif current.data == target:
            return current.data

    return current_largest 

def _build_bst():
    r = Node(10)
    r.left = Node(8)
    r.left.right = Node(9)
    r.right = Node(16)
    r.right.left = Node(13)
    r.right.right = Node(17)
    r.right.right.right = Node(20)
    return r

if __name__ == "__main__":
    root = _build_bst()

    print(FloorInBST(root,13))