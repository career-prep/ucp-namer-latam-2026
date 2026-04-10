class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    # Returns first item in the Queue. O(1) time.
    def peek(self):
        if self.front:
            return self.front.data
        else:
            return None
        
    
    # adds x to the back of the queue. O(1) time.
    def enqueue(self, x):

        newNode = Node(x)

        # Empty Queue
        if self.front == None and self.back == None:
            self.front = newNode
            self.back = newNode
        else:
            # Queue is not empty
            self.back.next = newNode
            self.back = newNode


    # Removes and returns first element in the queue. O(1) time.
    def dequeue(self):
        
        # Empty Queue
        if not self.front:
            return None
        
        saveVal = self.front.data
        
        # Removing the only element
        if self.front == self.back:
            self.front = None
            self.back = None
            return saveVal

        # There is more than one element in queue if we get here
        temp = self.front
        self.front = self.front.next
        temp.next = None
        # We don't need to sever the original front from the queue since the queue consisits of what is between front and back (inclusive), but I will do it anyway.

        return saveVal
    

    # returns a boolean indicating whether the queue is empty. O(1) time.
    def isEmpty(self):
        if self.front == None and self.back == None:
            return True
        else:
            return False

        

        


