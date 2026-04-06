class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insertAtFront(head, val):
        new_node = Node(val)
        new_node.next = head
        return new_node

class Stack:
    def __init__(self):
        self.head = None
 
    def top(self):
        # O(1) time
        if self.head is None:
            return None
        return self.head.data
 
    def push(self, x):
        # O(1) time
        self.head = Node.insertAtFront(self.head, x)
 
    def pop(self):
        # O(1) time
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        return val
 
    def isEmpty(self):
        # O(1) time
        return self.head is None