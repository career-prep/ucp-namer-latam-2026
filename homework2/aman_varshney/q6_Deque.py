# spent 15 minutes

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        

class Deque:
    def __init__(self) -> None:
        self.front = None
        self.back = None
    
    def front(self):
        """Returns first item. O(1)"""
        return self.front.data if self.front else None
        
    def back(self):
        """Returns last item. O(1)"""
        return self.back.data if self.back else None
        
    def pushBack(self, x):
        """Adds `x` to the back of the deque. O(1)"""
        if not self.front: # first element case
            new_node = Node(x) 
            self.front = new_node
            self.back = new_node
            return

        new_node = Node(x)
        new_node.prev = self.back
        self.back.next = new_node
        self.back = new_node
        
    def pushFront(self, x):
        """Adds `x` to the front. O(1)"""
        if not self.front: # first element case
            new_node = Node(x) 
            self.front = new_node
            self.back = new_node
            return
        
        new_node = Node(x)
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node
        
    def popFront(self):
        """Removes and returns value at front of deque. O(1)"""
        if not self.front: # empty case
            return None
        
        if self.front == self.back: # one element case
            x = self.front.data
            self.front = None
            self.back = None
            return x    
        
        x = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        return x
    
    def popBack(self):
        """Removes and returns value at back of deque. O(1)"""
        if not self.back: # empty case
            return None
        
        if self.front == self.back: # one element case
            x = self.front.data
            self.front = None
            self.back = None
            return x    
        
        x = self.back.data
        self.back = self.back.prev
        self.back.next = None
        return x
        
    def isEmpty(self):
        """True if deque is empty. O(1)"""
        return (self.front is None)