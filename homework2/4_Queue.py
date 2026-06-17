class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def peek(self):
        if not self.front:
            return None
        return self.front.data

    def enqueue(self, x):
        new_node = Node(x)

        if not self.back:
            self.front = self.back = new_node
            return

        self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        if not self.front:
            return None

        val = self.front.data
        self.front = self.front.next

        if not self.front:
            self.back = None

        return val

    def isEmpty(self):
        return self.front is None