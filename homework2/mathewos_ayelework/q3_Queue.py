class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):  # O(1)
        if self.isEmpty():
            return None
        return self.head.data

    def enqueue(self, x):  # O(1)
        new_node = Node(x)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):  # O(1)
        if self.isEmpty():
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def isEmpty(self):  # O(1)
        return self.head is None


print("Queue Results:")

q = Queue()
print(q.isEmpty())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.isEmpty())

print(q.dequeue())
print(q.dequeue())
print(q.peek())

q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())
print(q.dequeue())
