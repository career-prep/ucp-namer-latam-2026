"""
20 minutes
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def Front(self):
        if self.head is None:
            return None
        return self.head.data

    def Back(self):
        if self.tail is None:
            return None

        return self.tail.data

    def PushFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node

    def PushBack(self, data):
        new_node = Node(data)
        if self.head is None:
            self.PushFront(data)
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def PopFront(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        cur = self.head.next
        cur.prev = None
        self.head = cur
    def PopBack(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        cur = self.tail.prev
        cur.next = None
        self.tail = cur
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False


