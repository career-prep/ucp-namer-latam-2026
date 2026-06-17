class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def min(self):
        if self.root is None:
            return -1
        
        curr = self.root
        
        while curr.left:
            curr = curr.left
            
        return curr.data 
    
    def max(self):
        if self.root is None:
            return -1
        
        curr = self.root
        
        while curr.right:
            curr = curr.right
            
        return curr.data 
    
    def contains(self, val):
        curr = self.root
        while curr:
            if curr.data < val:
                curr = curr.right
                
            elif curr.data > val:
                curr = curr.left
                
            elif curr.data == val:
                return True
            
        return False
    
    def insert(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        curr = self.root
        
        while True:
            if val < curr.data:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left

            elif val > curr.data:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right

            else:
                return
            
    def delete(self, val):
        def dfs(node, val):
            if not node:
                return None

            if val < node.data:
                node.left = dfs(node.left, val)

            elif val > node.data:
                node.right = dfs(node.right, val)

            else:
                if not node.left and not node.right:
                    return None

                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                succ = node.right
                while succ.left:
                    succ = succ.left

                node.data = succ.data
                node.right = dfs(node.right, succ.data)

            return node

        self.root = dfs(self.root, val)
