def min(root):
    if not root:
        return -1 # assuming if there is no root, no integer hence return -1
    curr = root
    
    while curr.left:
        curr = curr.left
    return curr

def max(root):
    if not root:
        return -1 #similar assumption as def min(root)
    
    curr = root
    while curr.right:
        curr = curr.right

    return curr

def contains(root, val):
    if not root:
        return False
    
    # i have two approahces in mind first is with 
    ## simply finding using left or right by comparing val with root.val
    ## lets implement this first
    curr = root

    if curr.data == val:
        return True
    
    if curr.data < val:
        return contains(curr.right, val)
    else:
        return contains(curr.left, val)


    ## second is by using any kind of traversal, but instead of printing we just compare 
        ## dont know if this is the right approach or not but will try
def inorder(root, arr):
    curr = root
    if curr is None:
        return
    inorder(root.left, arr)
    arr.add(root.left.data)
    inorder(root.right, arr)

def isPresent(root, val):
    arr = []
    inorder(root, arr)
    return val in arr

def insert(root, val):
    #initially considered that the root is valid and no duplicates present and val not present
    if root is None:
        return Node(val) # type: ignore

    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

#helper function
def getSucc(root):
    root = root.right
    while root and root.left:
        root = root.left
    return root


#assumption: the given val exists in the tree
def delete(root, val):
    # if the root does not exists:
    if not root: return root

    #three conditions here
    ## when the node(to be removed) does not have any children
 
    ## when the node(to be removed) has one children: can be left or right

    ## when the node(to be removed) has two children

    if root.data < val:
        root.right = delete(root.right, val)
    elif root.data > val:
        root.left = delete(root.left, val)

    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        #case where node to be removed has 2 children
        succ = getSucc(root)
        root.data = succ.data
        root.right = delete(root.right, succ.data)

    return root


        

