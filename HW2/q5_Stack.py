class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
    

class Stack:
    def __init__(self):
        self.top_node=None
    
    def top(self):
        if self.top_node==None:
            return None
        return self.top_node.data
    
    def push(self,x): # 3 -> 2 ->1, push 4 => 4->3->2->1
        node=Node(x)
        
        if self.top_node ==None:
            self.top_node=node
            return 
        
        node.next=self.top_node
        self.top_node=node
        return
    
    def pop(self):
        if self.top_node==None:
            return None
        
        returned_val= self.top_node.data
        self.top_node=self.top_node.next
        return returned_val
    
    def isEmpty(self):
        if self.top_node==None:
            return True
        return False
    
    
    


        