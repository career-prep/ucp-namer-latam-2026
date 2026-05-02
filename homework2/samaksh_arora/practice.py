#Given a node, each node has a value, which is unset. eahc node has a left and right child. 

def height(root):
    count = 1
    return helper(root)
   
def helper(root):
    if not root.left and not root.right:
        count = 1
        root.val = count
        return
        
    self.height(root.left)
    self.height(root.right)

    count = 1 + max(root.left.val, root.right.val)
    root.val = count

        
    