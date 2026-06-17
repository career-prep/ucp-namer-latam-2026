class Deque:
    # basically same as queue but we support push/pop from BOTH ends
    # doubly LL is perfect for this
    def __init__(self):
        self.head = None
        self.tail = None
 
    # Time: O(1)
    def front(self):
        if self.head is None:
            return None
        return self.head.data
 
    # Time: O(1)
    def back(self):
        if self.tail is None:
            return None
        return self.tail.data
 
    # add to back
    # Time: O(1)
    def pushBack(self, x):
        new_node = DoublyNode(x)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
 
    # add to front
    # Time: O(1)
    def pushFront(self, x):
        new_node = DoublyNode(x)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
 
    # Time: O(1)
    def popFront(self):
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return val
 
    # Time: O(1)
    def popBack(self):
        if self.tail is None:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return val
 
    # Time: O(1)
    def isEmpty(self):
        return self.head is None
