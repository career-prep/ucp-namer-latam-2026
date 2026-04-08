#Queue Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue: 
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self): #O(1)
        if self.head:
            return self.head.data
        return None
    
    def enqueue(self, val): #O(1)
        newNode = Node(val)
        if not self.tail:
            self.head = newNode
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self): #O(1)
        if not self.head:
            return None
        curr = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            return curr.data
        self.head = self.head.next
        return curr.data
    
    def isEmpty(self): #O(1)
        return self.head is None
    