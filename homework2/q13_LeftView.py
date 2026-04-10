# Level order (breath-first) traversal
# O(n) Time Complexity
# O(n) Space Complexity, in the worst case, the queue of each level holds at most n/2 elements. Also, in a skewed tree, res array holds n elements
# Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree

from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def leftView(root):

    res = []

    if root == None:
        return res
    
    # BFS needs a queue
    q = deque()

    q.append(root)

    # while queue is not empty...
    while q:
        levelSize = len(q)

        
        poppedLeftMost = False

        # This part iterates over each level
        for i in range(levelSize):
            node = q.popleft()

            if node:
                # Make sure we only add the leftmost element of each level
                if poppedLeftMost == False:
                    res.append(node.data)
                    poppedLeftMost = True

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)



    return res


# 27 minutes


# Test Cases

# Binary Tree 1
root1 = TreeNode(7)
root1.left = TreeNode(8)
root1.right = TreeNode(3)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(13)
root1.right.left.left = TreeNode(20)
root1.right.right.left = TreeNode(14)
root1.right.right.left.right = TreeNode(15)

# Binary Tree 2
root2 = TreeNode(7)
root2.left = TreeNode(20)
root2.right = TreeNode(4)
root2.left.left = TreeNode(15)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(8)
root2.right.right = TreeNode(11)

print(leftView(root1))
print(leftView(root2))






    
