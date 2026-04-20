# Question 6: Deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        # Time and Space: O(1)
        return self.head.data

    def back(self):
        # Time and Space: O(1)
        return self.tail.data

    def pushBack(self, x):
        # Time and Space: O(1)
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pushFront(self, x):
        # Time and Space: O(1)
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def popFront(self):
        # Time and Space: O(1)
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def popBack(self):
        # Time and Space: O(1)
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def isEmpty(self):
        # Time and Space: O(1)
        return self.head is None

# time: 25 minutes
