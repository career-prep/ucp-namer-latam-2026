# spent 15 minutes
# Time complexity - O(n)
# Space complexity - O(1)
# Search BST


class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right
        
        
def floor(tree, target):
    if not tree:
        return None
    
    curr = tree
    max_floor = None
    while curr:
        data = curr.data
        if data < target:
            max_floor = data
            curr = curr.right
        elif data > target:
            curr = curr.left
        else: # equal -> max possible floor
            return data
        
    return max_floor 


if __name__ == "__main__":
    root1 = Node(10)
    root1.left = Node(8)
    root1.right = Node(16)
    root1.left.right = Node(9)
    root1.right.left = Node(13)
    root1.right.right = Node(17)
    root1.right.right.right = Node(20)
    print("Test 1")
    print("Actual: ", floor(root1, 13))
    print("Expected: 13")
    
    print()
    
    root2 = Node(10)
    root2.left = Node(8)
    root2.right = Node(16)
    root2.left.right = Node(9)
    root2.right.left = Node(13)
    root2.right.right = Node(17)
    root2.right.right.right = Node(20)
    print("Test 2")
    print("Actual: ", floor(root2, 15))
    print("Expected: 13")