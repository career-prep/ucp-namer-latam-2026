# Technique: Depth-first traversal (in-order / generic DFS with bounds)
# Time:  O(n) - visit every node once
# Space: O(h) - recursion stack, h = height of tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBSTHelper(node, min_val, max_val):
    if node is None:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return (isBSTHelper(node.left, min_val, node.data) and
            isBSTHelper(node.right, node.data, max_val))
 
def isBST(root):
    return isBSTHelper(root, float('-inf'), float('inf'))

root1 = Node(10)
root1.left = Node(8)
root1.right = Node(16)
root1.left.right = Node(9)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)
 
root2 = Node(10)
root2.left = Node(8)
root2.right = Node(16)
root2.left.right = Node(9)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)

root3 = Node(10)
root3.left = Node(5)
root3.right = Node(15)
root3.left.left = Node(1)
root3.left.right = Node(12)

root4 = Node(10)
root4.left = Node(10)
 
print(isBST(root1))
print(isBST(root2)) 
print(isBST(root3))
print(isBST(root4))   
print(isBST(None))  
print(isBST(Node(5))) 
