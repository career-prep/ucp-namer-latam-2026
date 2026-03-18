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
        """Return the first item in the deque. O(1)."""
        if self.head:
            return self.head.data
        return -1        

    def back(self):
        """Return the last item in the deque. O(1)."""
        if self.tail:
            return self.tail.data
        return -1

    def pushBack(self, x):
        """Add x to the back of the deque. O(1)."""
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
            return
        
        new_node = Node(x)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pushFront(self, x):
        """Add x to the front of the deque. O(1)."""
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
            return
        
        new_head = Node(x)
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head

    def popFront(self):
        """Remove and return the first item in the deque. O(1)."""
        if not self.head:
            return -1
        if not self.head.next:
            first = self.head.data
            self.head = None
            self.tail = None
            return first

        first = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return first

    def popBack(self):
        """Remove and return the last item in the deque. O(1)."""
        if not self.tail:
            return -1
        if not self.tail.prev:
            last = self.tail.data
            self.head = None
            self.tail = None
            return last           
        
        last = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return last

    def isEmpty(self):
        """Return whether the deque is empty. O(1)."""
        if not self.head:
            return True
        return False

