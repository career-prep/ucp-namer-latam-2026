#40 minutes
#Technqiue: Level-order (breadth-first) traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        array.append(root.data)
        return array

    result = []
    queue = [root]
    
    while len(queue) > 0:
        level_size = len(queue)
        
        for i in range(level_size):
            Node = queue.pop(0)

            if i == 0:
                result.append(Node.data)

            if Node.left is not None:
                queue.append(Node.left)
            if Node.right is not None:
                queue.append(Node.right)    
    return result

def _build_bst():
    r = Node(7)
    r.left = Node(8)
    r.right = Node(3)
    r.left.left = Node(9)
    r.left.left.left = Node(20)
    r.left.right = Node(13)
    r.left.right.left = Node(14)
    r.left.right.left.right = Node(15)
    return r

if __name__ == "__main__":
    root = _build_bst()

    print(LeftView(root))