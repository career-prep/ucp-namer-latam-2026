from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def bfs_binary_tree(root):
    # exception handling: if binary tree is empty
    if not root:
        return

    # initializing queue
    queue = deque([root])
    print(queue)
    
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        
        # Enqueue left child
        if node.left:
            queue.append(node.left)
            
        # Enqueue right child
        if node.right:
            queue.append(node.right)

# Example Usage:
#      1
#     / \
#    2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

bfs_binary_tree(root)  # Output: 1 2 3
