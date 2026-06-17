# Data Structure Implementation: Queue (using singly linked list)
# time complexity per method noted inline
# 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  # front of queue
        self.tail = None  # back of queue

    def peek(self):  # O(1)
        if not self.head:
            return None
        return self.head.data

    def enqueue(self, x):  # O(1)
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):  # O(1)
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def isEmpty(self):  # O(1)
        return self.head is None

# test cases
q = Queue()
assert q.isEmpty() == True
assert q.dequeue() is None

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert q.peek() == 1
assert q.isEmpty() == False

assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.peek() == 3
assert q.dequeue() == 3
assert q.isEmpty() == True

print("yay!!")
