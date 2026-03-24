class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self): # Time, Space Complexities: O(1), O(1)

        #1. Return the data at the head without removing it
        if self.isEmpty():
            return None
        return self.head.data

    def enqueue(self, x): # Time, Space Complexities: O(1), O(1
        new_node = Node(x)

        # If queue is empty, new node is both head and tail
        if self.tail is None:
            self.head = self.tail = new_node
            return
        # Add new node to the end and update tail reference
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self): # Time, Space Complexities: O(1), O(1)

        #Handle empty queue case
        if self.isEmpty():
            return None
        
        #Store data, shift head forward, and return data
        data = self.head.data
        self.head = self.head.next
        #If head becomes None, the queue is now empty; reset tail
        if self.head is None:
            self.tail = None
        return data

    def isEmpty(self): # Time, Space Complexities: O(1), O(1)
        #Queue is empty if the head reference is None
        return self.head is None