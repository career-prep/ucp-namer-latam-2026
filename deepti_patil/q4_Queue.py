class Queue:
    # using a doubly linked list under the hood so both ends are O(1)
    def __init__(self):
        self.head = None  # front of queue (dequeue from here)
        self.tail = None  # back of queue (enqueue here)
 
    # Time: O(1)
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
 
    # add to the back
    # Time: O(1)
    def enqueue(self, x):
        new_node = DoublyNode(x)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
 
    # remove from the front
    # Time: O(1)
    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None  # list is empty now
        return val
 
    # Time: O(1)
    def isEmpty(self):
        return self.head is None
 
