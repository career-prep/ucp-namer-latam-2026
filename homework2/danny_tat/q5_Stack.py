# Question 5: Stack

class Stack:
    def __init__(self):
        self.head = None

    def top(self):
        # Time and Space: O(1)
        return self.head.data

    def push(self, x):
        # Time and Space: O(1)
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        # Time and Space: O(1)
        val = self.head.data
        self.head = self.head.next
        return val

    def isEmpty(self):
        # Time and Space: O(1)
        return self.head is None

# time: 20 minutes
