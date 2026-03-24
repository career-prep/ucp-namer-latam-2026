class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def top(self):
        
        if self.top is None:
            return None
        
        return self.top.data
    
    def push(self, x):

        new_Node = Node(x)

        if self.top is None:
            self.top = new_Node
        else:
            new_Node.next = self.top
            self.top = new_Node
    
    def pop(self):

        if self.top is None:
            return None
        
        x = self.top.data
        self.top = self.top.next
        
        return x
    
    def isEmpty(self):

        if self.top is None:
            return True
        else:
            return False
        
# 7 mins