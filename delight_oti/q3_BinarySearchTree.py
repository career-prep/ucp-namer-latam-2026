class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None   

    def min(self):
        
        curr = self.root

        while curr.left:
            curr = curr.left
        
        return curr.data
    
    def max(self):

        curr = self.root

        while curr.right:
            curr = curr.right

        return curr.data
    
    def contains(self, val):

        curr = self.root

        while curr:
            if curr.data == val:
                return True
            elif val > curr.data:
                curr = curr.right 
            else:
                curr = curr.left
        
        return False
    
    def insert (self, val):
    
        def insert_helper (root, val):

            if root is None:
                return Node(val)
            
            if val > root.data:
                root.right = insert_helper(root.right, val)
            else:
                root.left = insert_helper(root.left, val)
            
            return root
        
        self.root = insert_helper(self.root, val)
    
    # def delete (self, val):

    #     root = self.root

    #     if root is None:
    #         return None
        
    #     if val > root.val:
    #         root.right = self.delete(root.right, val)
    #     elif val < root.val:
    #         root.left = self.delete(root.left, val)
    #     else:
        
        # at end
        # at middle
        # at beginning

#40 mins cus of delete