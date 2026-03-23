# Data Structure Implementation: Deque (using doubly linked list)
# time complexity per method noted inline
# 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # back

    def front(self):  # O(1)
        if not self.head:
            return None
        return self.head.data

    def back(self):  # O(1)
        if not self.tail:
            return None
        return self.tail.data

    def pushBack(self, x):  # O(1)
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pushFront(self, x):  # O(1)
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def popFront(self):  # O(1)
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def popBack(self):  # O(1)
        if not self.tail:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def isEmpty(self):  # O(1)
        return self.head is None

# test cases
d = Deque()
assert d.isEmpty() == True

d.pushBack(1)
d.pushBack(2)
d.pushFront(0)
assert d.front() == 0
assert d.back() == 2

assert d.popFront() == 0
assert d.popBack() == 2
assert d.front() == 1
assert d.back() == 1
assert d.popFront() == 1
assert d.isEmpty() == True

d.pushFront(5)
d.pushFront(3)
d.pushBack(7)
assert d.front() == 3
assert d.back() == 7
assert d.popBack() == 7
assert d.popBack() == 5

print("yay!!")
