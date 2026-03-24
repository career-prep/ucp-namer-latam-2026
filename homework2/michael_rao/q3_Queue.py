class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if not self.head:
            return None
        return self.head.val
    # time: O(1)

    def enqueue(self, x):
        new_node = Node(x, None, self.tail)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    # time: O(1)

    def dequeue(self):
        if not self.head:
            return None
        first_val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return first_val
    # time: O(1)

    def isEmpty(self):
        return self.head == None
    # time: O(1)