# spent 5 minutes

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        

class Stack:
    def __init__(self, head) -> None:
        self.head = head
        
    def top(self):
        """Returns top item. O(1)"""
        return self.head.data
    
    def push(self, x): 
        """Adds `x` to the stack. O(1)"""
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        """Pops top item in stack. O(1)"""
        if not self.head: # empty case
            return None
        
        x = self.head.data
        self.head = self.head.next
        return x
        
    def isEmpty(self):
        """Returns true if the stack is empty. O(1) """
        return (self.head is None)