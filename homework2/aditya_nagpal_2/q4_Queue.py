#queue
class myQueue:
    def __init__(self, capacity):
        
        # Maximum number of elements the queue can hold
        self.capacity = capacity
        
        # Array implementation
        self.arr = [0] * capacity
        
        # elements in the queue
        self.size = 0

    def peek(self):
        if self.size == 0:
            return "the queue is empty"
        return self.arr[0]
    
    def enqueue(self, x):
        if self.size == self.capacity:
            return "queue is full"
        self.arr[self.size] = x
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "the queue is empty"
        first_element = self.arr[0]
        for i in range(1, self.size):
            self.arr[i-1] = self.arr[i]
        self.size -= 1

        return first_element
    
    def isEmpty(self):
        return self.size == 0
    
    
            
