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

        if self.head is None:
            return None
        
        return self.head.data
    
    def back(self):

        if self.tail is None:
            return None
        
        return self.tail.data
    
    def pushBack(self, x):

        new_node = Node(x)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def pushFront(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def popFront(self):

        if self.head is None:
            return None
        
        val = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None
        
        return val
    
    def popBack(self):

        if self.tail is None:
            return None
        
        val = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return val
    
    def isEmpty(self):
        
        if self.head is None:
            return True
        
        else:
            return False

# 15 mins