# Technique: Level-order (breadth-first) traversal
# Time: O(n)
# Space: O(n) - queue can hold up to n/2 nodes at the widest level
 
# BFS  we process nodes level by level at each level the first node we see is the leftmost one
 
from collections import deque
 
def leftView(root):
    if root is None:
        return []
 
    result = []
    queue = deque([root])
 
    while queue:
        level_size = len(queue)  # how many nodes are at this level
 
        for i in range(level_size):
            node = queue.popleft()
 
            # only grab the first node of each level (leftmost)
            if i == 0:
                result.append(node.data)
 
            # add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
    return result
 
