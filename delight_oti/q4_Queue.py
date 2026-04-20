class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def peek(self):
        
        return self.front.data
    
    def enqueue(self, x):

        newNode = Node(x)
        
        if self.front is None:
            self.front = newNode
            self.back = newNode
        
        else:
            self.back.next = newNode
            self.back = newNode
    
    def dequeue(self):

        if self.front is None:
            return None
        else:
            x = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.back = None
        
        return x
    
    def isEmpty(self):
        
        if self.front is None:
            return True
        else:
            return False
        
# 16mins