class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root):
    """
    Given a binary tree root, determine whether it is a binary search tree.

    Time: O(n)
    Space: O(h = tree height)
    """
    def dfs(node, low, high):
        if not node:
            return True
        
        if not (low < node.data < high):
            return False
        
        return dfs(node.left, low, node.data) and dfs(node.right, node.data, high)
    
    return dfs(root, float("-inf"), float("inf"))

# Example 1 (expected True)
root1 = Node(10)
root1.left = Node(8)
root1.left.right = Node(9)

root1.right = Node(16)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

# Example 2 (expected False)
root2 = Node(10)
root2.left = Node(8)
root2.left.right = Node(9)

root2.right = Node(16)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)


print(isBST(root1))
print(isBST(root2))

