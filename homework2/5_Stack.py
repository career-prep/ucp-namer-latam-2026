class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None

    def top(self):
        if not self.top_node:
            return None
        return self.top_node.data

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.top_node:
            return None

        val = self.top_node.data
        self.top_node = self.top_node.next
        return val

    def isEmpty(self):
        return self.top_node is None