class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.back_node = None
    # O(1)
    def peek(self):
        if not self.front_node:
            return None
        return self.front_node.data

    # O(1)
    def enqueue(self, x):
        new_node = Node(x)
        if not self.back_node:  # empty queue
            self.front_node = self.back_node = new_node
            return
        self.back_node.next = new_node
        self.back_node = new_node

    # O(1)
    def dequeue(self):
        if not self.front_node:
            return None
        val = self.front_node.data
        self.front_node = self.front_node.next
        if not self.front_node:  # queue became empty
            self.back_node = None
        return val

    # O(1)
    def isEmpty(self):
        return self.front_node is None