class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root


def inorderTraversal(root):
    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

def preorderTraversal(root):
    res = []

    def dfs(node):
        if not node:
            return

        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res

def postorderTraversal(root):
    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
        
    dfs(root)
    return res

def find_min(root):
    if not root:
        return None
    
    current = root
    while current.left:
        current = current.left
        
    return current.val
#time complexity = 0(log n)
#space complexity = 0(1)

def find_max(root):
    if not root:
        return None
    
    current = root
    while current.right:
        current = current.right
    return current.val
#time complexity = 0(log n) or 0(h)
#space complexity = 0(1)

def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return max(left_height, right_height) + 1

#time complexity = 0(n)
#space complexity = 0(h)

def find_level(root, target, current_level=1):
    if root is None:
        return 0
    
    if root.val == target:
        return current_level
    
    left_side = find_level(root.left, target, current_level + 1)
    if left_side != 0:
        return left_side
    
    return find_level(root.right, target, current_level + 1)

def contains(root, val):
    if root is None:
        return False
    if root.val == val:
        return True

    if val < root.val:
        return contains(root.left, val)
    return contains(root.right, val)
#time complexity = 0(log n)
#space complexity = 0(h)

def insert_recursive(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = insert_recursive(root.left, val)
    elif val > root.val:
        root.right = insert_recursive(root.right, val)

    return root
#time complexity = 0(log n)
#space complexity = 0(h)

def deleteNode(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    
    else:
        # Case 1 & 2 No child or only one child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case 3 Two children
        # Get the smallest node in the right subtree
        temp = root.right
        while temp.left:
            temp = temp.left
        
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root

values = [5, 3, 7, 2, 4, 6, 8]

root = None
for v in values:
    root = insert(root, v)

result = inorderTraversal(root)
print("Inorder Traversal:", result)

result = preorderTraversal(root)
print("Preorder Traversal:", result)

result = postorderTraversal(root)
print("Postorder Traversal:", result)

result = find_min(root)
print("Minimum Value:", result)

result = find_max(root)
print("Maximum Value:", result)

result = height(root)
print("Height:", result)

result = find_level(root, 2)
print("Level of a Node:", result)

result = contains(root, 2)
print("The node is found in the tree:", result)

root = insert_recursive(root, 9)
print("After insert_recursive(9), inorder:", inorderTraversal(root))
root = insert_recursive(root, 4)
print("After insert_recursive(4), inorder:", inorderTraversal(root))

root = deleteNode(root, 4)
print("After insert_recursive(4), inorder:", inorderTraversal(root))