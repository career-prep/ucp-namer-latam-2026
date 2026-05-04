# Approach:
# Use level-order traversal (BFS)
# For each level, the first node we see is the leftmost node
# So for every level, record the first element

# Time Complexity: O(n)


# Space Complexity: O(n)


from collections import deque

def leftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # first node of this level → left view
            if i == 0:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result




def bfs(root):
    if not root: return None
    res = []
    q = deque()

    q.append(root)
    
    while q:
        len_q = len(q)
        arr = []

        for _ in range(len_q):
            node = q.popleft()
            arr.append(node.data)

            if root.left:
                q.append(root.left)

            if root.right:
                q.append(root.right)

        res.append(arr)

        #time Complexirty: priocessing everysingle node(total nodes n): O(n)



    #given: a binary tree
    #return: the array with left most elements at each level

    #bruteforce

def leftView(root):
    if not root:
        return None
    
    res = []
    queue = deque()

    queue.append(root)

    while queue:
        len_queue = len(queue)
        

        for i in range(len_queue):
            node = queue.popleft()
            if i == 0:
                res.append(node.data)

            if node.left :
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        

    return res

