class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque():
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if not self.head:
            return None
        return self.head.val
    # time: O(1)

    def back(self):
        if not self.tail:
            return None
        return self.tail.val
    # time: O(1)

    def pushBack(self, x):
        new_node = Node(x, None, self.tail)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    # time: O(1)

    def pushFront(self, x):
        new_node = Node(x, self.head, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        self.head = new_node
    # time: O(1)

    def popBack(self):
        if not self.tail:
            return None
        last_val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return last_val
    # time: O(1)

    def popFront(self):
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