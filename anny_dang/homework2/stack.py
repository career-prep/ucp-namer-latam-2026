class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def top(self):
        """Return the top item in the stack. O(1)."""
        if not self.head:
            return -1
        return self.head.data

    def push(self, x):
        """Add x to the top of the stack. O(1)."""
        new_head = Node(x)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        """Remove and return the top item in the stack. O(1)."""
        if not self.head:
            return -1

        first = self.head.data
        self.head = self.head.next
        return first

    def isEmpty(self):
        """Return whether the stack is empty. O(1)."""
        return self.head is None
