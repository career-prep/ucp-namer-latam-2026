# spent 20 minutes
# Time complexity - O(n)
# Space complexity - O(n)
# Inorder traversal


class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right


def isBST(tree):
    """Returns true if `tree` is a BST."""
    if not tree: # empty case
        return True
    # create a list by inorder
    curr = tree
    values = []
    
    # helper
    def helper(node, values):
        if not node: # empty case
            return
        
        helper(node.left, values)
        values.append(node.data)
        helper(node.right, values)
        
    helper(curr, values)
    
    # check if values is increasing strictly
    prev = values[0]
    for i in range(1, len(values)):
        if values[i] <= prev:
            return False
        prev = values[i]
        
    return True
    
            
    
if __name__ == '__main__':
    # correct bst test
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(7)
    root1.left.left = Node(2)
    root1.left.right = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(8)
    print("tree 1", isBST(root1))
    print("Expected: True")
    
    # incorrect
    root2 = Node(5)
    root2.left = Node(3)
    root2.right = Node(7)
    root2.left.left = Node(2)
    root2.left.right = Node(6) # breaks
    print("tree 2", isBST(root2))
    print("Expected: False")