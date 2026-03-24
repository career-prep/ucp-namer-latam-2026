class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = self.back = None

    # Time complexity: O(1)
    def peek(self):
        if not self.front:
            print("peek from empty queue")
            return None
        return self.front.data

    # Time complexity: O(1)
    def enqueue(self, x):
        node = Node(x)
        if not self.back:
            self.front = self.back = node
        else:
            self.back.next = node
            self.back = node

    # Time complexity: O(1)
    def dequeue(self):
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.back = None
        return val
    
    # Time complexity: O(1)
    def isEmpty(self):
        return self.front is None
