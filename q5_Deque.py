class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def _init_(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def pushFront(self, x: int):
        new_node = Node(x)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pushBack(self, x: int):
        new_node = Node(x)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def popFront(self):
        if self.isEmpty():
            raise IndexError("Pop from empty deque")
        
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # List is now empty
        return data

    def popBack(self):
        if self.isEmpty():
            raise IndexError("Pop from empty deque")
        
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None  # List is now empty
        return data

    def front(self):
        if self.isEmpty():
            raise IndexError("Front from empty deque")
        return self.head.data

    def back(self):
        if self.isEmpty():
            raise IndexError("Back from empty deque")
        return self.tail.data