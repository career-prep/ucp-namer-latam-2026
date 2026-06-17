# Implement a Queue using a linked list with the following methods:
# peek, enqueue, dequeue, isEmpty.
# All operations should be O(1).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def is_empty(self):
        return self.head is None


q = Queue()
print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())

# peek: O(1)
# enqueue: O(1)
# dequeue: O(1)
# isEmpty: O(1)
# Spent 35 mins
