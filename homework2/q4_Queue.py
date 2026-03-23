# spent 15 minutes

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None # front
        self.tail = None # back
        
    def peek(self): 
        """Returns first element on top. O(1)"""
        return self.head.data if self.head else None
    
    def enqueue(self, x): 
        """Adds x to the back of the queue. O(1)"""
        # create new node
        new_node = Node(x)
        
        # link
        if not self.tail: # empty case
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def dequeue(self):
        """Pops the first item from the queue. O(1)"""
        if not self.head:
            return None # empty case
        
        x = self.head.data
        self.head = self.head.next # update head
        
        if not self.head: # one element case
            self.tail = None
            
        return x
        
    def isEmpty(self):
        return (self.head == None)
            