# Question 4: Queue

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        # Time and Space: O(1)
        return self.head.data

    def enqueue(self, x):
        # Time and Space: O(1)
        new_node = SinglyNode(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        # Time and Space: O(1)
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def is_empty(self):
        # Time and Space: O(1)
        return self.head is None

# time: 20 minutes
