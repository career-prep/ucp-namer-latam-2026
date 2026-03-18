class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        """Return the first item in the queue. O(1)."""
        if self.head:
            return self.head.data
        return -1 

    def enqueue(self, x):
        """Add x to the back of the queue. O(1)."""
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
            return
        
        new_node = Node(x)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def dequeue(self):
        """Remove and return the first item in the queue. O(1)."""
        if not self.head:
            return -1
        if not self.head.next:
            first = self.head.data
            self.head = None
            self.tail = None
            return first
        
        first = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return first

    def isEmpty(self):
        """Return whether the queue is empty. O(1)."""
        if not self.head:
            return True
        return False

