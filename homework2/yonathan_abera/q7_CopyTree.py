# Technique: Depth-first traversal (pre-order)
# Time:  O(n) - visit every node once
# Space: O(n) - store n nodes + O(h) recursion stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def copyTree(root):
    if root is None:
        return None
    new_node = Node(root.data)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    return new_node

def tree_to_list(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
    return result
 
 
root1 = Node(10)
root1.left = Node(8)
root1.right = Node(16)
root1.left.right = Node(9)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)
 
root2 = Node(5)
 
root3 = Node(1)
root3.left = Node(2)
root3.left.left = Node(3)
 
print(tree_to_list(copyTree(root1)))  
print(tree_to_list(copyTree(root2)))   
print(tree_to_list(copyTree(root3)))  
print(tree_to_list(copyTree(None)))