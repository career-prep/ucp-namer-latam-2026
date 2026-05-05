class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left=left
        self.right=right
    


class BST:
    def __init__(self):
        self.root=None

    
    def min(self):
        if self.root==None:
            return None
        
        curr= self.root
        while curr.left:
            curr=curr.left
        
        min_val=curr.data
        return min_val

    def max(self):
        if self.root==None:
            return None
        
        curr=self.root
        while curr.right:
            curr=curr.right
        
        max_val=curr.data
        return max_val
    
    def contains(self,val):
        if self.root==None:
            return False
        
        curr=self.root
        while curr:
            if curr.data==val:
                return True
            elif curr.data>val:
                curr=curr.left
            else:
                curr=curr.right
        
        return False
    


    """
    logic:
        traverse through the whole tree until reaching the leaf
        if node.data<val => must go to the right subtree
        if node.data>val => must go to the left subtree
        if node.data=val => return (no operation)
    """

    def insert(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
            return 
        
        curr=self.root
        while curr:
            if curr.data==val:
                return
            
            if curr.data<val:
                if curr.right==None:
                    curr.right=node
                    return 
                else:
                    curr=curr.right
            else:
                if curr.left==None:
                    curr.left=node
                    return
                else:
                    curr=curr.left
        
        return 
    

    def insert_recursion(self,val):
        self.root=self.insert_helper(self.root,val)
    
    def insert_helper(self,parent, val):
        node = Node(val)
        #what is the smallet version of this problem: when tree is empty, just return the node
        #=> base case:
        if parent ==None:
            return node

        #if the node is not empty, we compare:
        # val< parent.data => move left
        # val> parent.data => move right
        #val = parent.data => dont need to handle since no operation
        #=> recursion step:
    
        if val< parent.data:
            parent.left= self.insert_helper(parent.left,val)
        elif val> parent.data:
            parent.right=self.insert_helper(parent.right,val)
        
        return parent

            
    
    """
    logic: 
        #traverse:
        #if val<parent.data => move left
        #if val>parent.data => move right

        #else: 
            #handle when we meet the deleted node: there will be 3 cases:
            # if the removed node is leaf => return None
            # if the removed node have 1 other node => 2 case: if have left node: return left node, it have right node: return right node
            #if the removed node have 2 other nodes: 
            #   find the smallest value in right subtree and replace the removed node with it
            #   after that, delete that smallest value to avoid duplciate
    
    """

    def delete(self,val):
        self.root= self.delete_helper(self.root, val)

    def delete_helper(self, parent, val):
        #base case: when the tree is empty, then just return None
        if parent==None:
            return None

        if val<parent.data:
            parent.left= self.delete_helper(parent.left,val)
        elif val> parent.data:
            parent.right=self.delete_helper(parent.right,val)
        else:
            if parent.right==None and parent.left==None:
                return None
            elif parent.right==None:
                return parent.left
            elif parent.left==None:
                return parent.right
            #when the removed node have 2 other nodes
            curr=parent.right
            while curr.left:
                curr=curr.left
            
            parent.data= curr.data
            parent.right= self.delete_helper(parent.right, curr.data)
        
        return parent


    

        

#####################
    def insert_method(self, val):
        node=Node(val)
        if self.root==None:
            self.root=node
            return
        
        curr=self.root
        while curr:
            if val==curr.data:
                return self.root

            elif val<curr.data:
                if curr.left:
                    curr=curr.left
                else:
                    curr.left=node
                    return 
            else:
                if curr.right:
                    curr=curr.right
                else:
                    curr.right=node
                    return 

        
        return

    def insert_recursion(self, val):
        self.root=self.helper(self.root,val)
        return self.root
    
    def help(curr, val):
        node =Node(val)

        #base case
        if curr==None:
            return node
        
        #travese all the way to the last node and traceback with call stack, insert to the leaf
        if val<curr.data:
            curr.left= helper(curr.left, val)
        elif val>curr.data:
            curr.right=helper(curr.right,val)
        
        #recursive case return; it will be the thing returned after the recursion stopped
        return curr


    def delete_recursion(self, val):
        return delete_help(self.root,val)
    
"""
    def delete_help(curr, val):
        node=Node(val)
        #base case (the simpliest case)
        if curr==None:
            return None
        
        #there gonna be 3 case:
        # if val < curr.data => move to the left
        # if val > curr.data => move to the right
        # if val == data:
        #   + if deleted_node have 0 child, just delete and set prev ptr to None
        #   + if deleted_node have 1 child => delete and set the prev ptr to that child
        #   + if deleted_node have 2 child => go to right, travel all the way to the left to
        #  get the left most on right subtree, then replace the value with the deleted node

        if val< curr.data:
            curr.left= delete_help(curr.left,val)
        elif val> curr.data:
            curr.right=delete_help(curr.right,val)
        else:
            if curr.right==None and curr.left==None:
                return None
            elif curr.right==None:
                return curr.left
            elif curr.left==None:
                return curr.right
            else:
                curr_track= curr.right

                while curr_track/left:
                    curr_track=curr_track.left
                
                curr.data= curr_track.data
                curr.right= delete_help(curr.right, curr.data) #reconstruct the right subtree so that it delete the left most node

        return curr

        
"""
        

        
            
        

    




        