# spent 10 minutes
# Time complexity - O(n)
# Space complexity - O(n) 
# Generic traversal

class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right
        
        
def copyTree(root):
    """Creates a deep copy of a tree and returns the root of new tree"""
    if not tree1:
        return None
    
    new_tree = Node(root.val)
    new_tree.right = copyTree(root.right)
    new_tree.left = copyTree(root.left)
    return new_tree


if __name__ == '__main__':
    # helper to print trees
    def printTree(node):
        if not node: 
            return 
        printTree(node.left)
        print(str(node.data), end = " ")
        printTree(node.right)
        
    # tree1 
    tree1 = Node(10)
    tree1.left = Node(5)
    tree1.right = Node(15)
    tree1.left.left = Node(4)
    tree1.left.right = Node(9)
    tree1.right.right = Node(20)
    # copied tree
    copied_tree1 = copyTree(tree1)
    # print trees
    print("Original tree")
    printTree(tree1)
    print()
    print("Copied tree")
    printTree(copied_tree1)
    print()
    # modify original 
    tree1.right.data = 17
    print("Modified Original tree")
    printTree(tree1)
    print()
    print("Copied tree")
    printTree(copied_tree1)
