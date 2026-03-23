class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None 
        
    def top(self):
        if self.head is None:
            return None
        return self.head.data
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.head is None:
            return None

        val = self.head.data
        self.head = self.head.next
        return val
    
    def isEmpty(self):
        return self.head is None