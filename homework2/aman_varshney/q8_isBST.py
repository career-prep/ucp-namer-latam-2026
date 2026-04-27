# spent 20 minutes
# Time complexity - O(n)
# Space complexity - O(1)
# Inorder traversal


class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right


# helper for making sure node is within range of bst
def helper(node, low, high):
    if not node: 
        return True
    
    if not (low < node.data < high): # out of bounds 
        return False
    
    # left child and right child and update bound
    return helper(node.left, low, node.data) and helper(node.right, node.data, high)


def isBST(tree):
    # root can be any number
    return helper(tree, float('-inf'), float('inf'))
            
    
if __name__ == '__main__':
    # correct bst test
    root1 = Node(10)
    root1.left = Node(8)
    root1.right = Node(16)
    root1.left.right = Node(9)
    root1.right.left = Node(13)
    root1.right.right = Node(17)
    root1.right.right.right = Node(20)
    print("tree 1", isBST(root1))
    print("Expected: True")
    
    # incorrect
    root2 = Node(10)
    root2.left = Node(8)
    root2.right = Node(16)
    root2.left.right = Node(9)
    root2.right.left = Node(13)
    root2.right.right = Node(17) 
    root2.right.right.right = Node(15) # breaks
    print("tree 2", isBST(root2))
    print("Expected: False")