# Implement a Deque (double-ended queue) using a doubly linked list with
# the following methods: front, back, pushBack, pushFront, popFront,
# popBack, isEmpty. All operations should be O(1).

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
        if self.is_empty():
            return None
        return self.head.data

    def back(self):
        if self.is_empty():
            return None
        return self.tail.data

    def push_back(self, x):
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def push_front(self, x):
        new_node = Node(x)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def pop_front(self):
        if self.is_empty():
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def pop_back(self):
        if self.is_empty():
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def is_empty(self):
        return self.head is None


d = Deque()
print(d.is_empty())
d.push_back(1)
d.push_back(2)
d.push_front(0)
print(d.front())
print(d.back())
print(d.pop_front())
print(d.pop_back())
print(d.pop_front())
print(d.is_empty())

# front: O(1)
# back: O(1)
# pushBack: O(1)
# pushFront: O(1)
# popFront: O(1)
# popBack: O(1)
# isEmpty: O(1)
# Spent 40 mins
