#Stack Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def top(self): #O(1)
        if self.head:
            return self.head.data
        return None
    
    def push(self, val): #O(1)
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self): #O(1)
        if not self.head:
            return None
        curr = self.head
        self.head = self.head.next
        return curr.data
    
    def isEmpty(self): #O(1)
        return self.head is None
    
        