class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None  # top of stack

    # O(1)
    def top(self):
        if not self.top_node:
            return None
        return self.top_node.data

    # O(1)
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node

    # O(1)
    def pop(self):
        if not self.top_node:
            return None
        val = self.top_node.data
        self.top_node = self.top_node.next
        return val

    # O(1)
    def isEmpty(self):
        return self.top_node is None