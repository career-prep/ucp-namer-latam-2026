#Double Ended Queue Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if not self.head:
            return None
        return self.head.data
    
    def back(self):
        if not self.tail:
            return None
        return self.tail.data
    
    def pushBack(self, val):
        newNode = Node(val)
        if not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail  
            self.tail.next = newNode
            self.tail = newNode
    
    def pushFront(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode  
            self.head = newNode

    def popFront(self):
        if not self.head:
            return None
        curr = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            return curr.data
        self.head = self.head.next
        self.head.prev = None 
        return curr.data
    
    def popBack(self):
        if not self.tail:
            return None
        curr = self.tail
        if self.tail.prev is None:
            self.head = None
            self.tail = None
            return curr.data
        self.tail = self.tail.prev  
        self.tail.next = None       
        return curr.data
    
    def isEmpty(self):
        return self.head is None