#technique: BFS
#time complexity: O(n)
#space complexity: O(n)

from collections import deque 

class Node:
    def __init__(self,data):
        self.val = data
        self.right = None
        self.left = None 

def LeftView(root):
    if root is None:
        return []

    q = deque()
    result = []
    q.append(root)

    while q:
        level = len(q)
        for i in range(level):
            current = q.popleft()
            if i == 0:
                result.append(current.val)

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    return result

root = Node(7)
root.left = Node(20)
root.right = Node(4)
root.right.left = Node(8)
root.right.right = Node(11)
root.left.left = Node(15)
root.left.right = Node(6)
    
res =LeftView(root)
print('test1: ')
print(res)

#time spent: 25 min