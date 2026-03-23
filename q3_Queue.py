class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Queue:
    def _init_(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, x: int):
        new_node = Node(x)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        
        removed_data = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        return removed_data

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.head.data