# 40 minutes
# Technqiue: Level-order (breadth-first) traversal
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def IsBST(root):
    def helper(node, low, high):
        if node is None:
            return True

        if not (low < node.data < high):
            return False
        
        return helper(node.left, low, node.data) and helper(node.right, node.data, high)
    return helper(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    a = Node(10)
    a.left = Node(8)
    a.left.right = Node(9)
    a.right = Node(16)
    a.right.left = Node(13)
    a.right.right = Node(17)
    a.right.right.right = Node(20)
    print(IsBST(a)) 
