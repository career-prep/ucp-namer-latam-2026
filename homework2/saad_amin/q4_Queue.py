class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def enqueue(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        val = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return val
    
    def isEmpty(self):
        return self.head is None