class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        #Track both ends to allow O(1) access
        self.head = None
        self.tail = None

    def front(self): # Time, Space Complexities: O(1), O(1)
        if self.isEmpty():
            return None
        return self.head.data

    def back(self): # Time, Space Complexities: O(1), O(1)
        if self.isEmpty():
            return None
        return self.tail.data

    def pushFront(self, x): # Time, Space Complexities: O(1), O(1)
        new_node = Node(x)

        #Link new node as the new head
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pushBack(self, x): # Time, Space Complexities: O(1), O(1)
        new_node = Node(x)
        #Link new node as the new tail
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def popFront(self): # Time, Space Complexities: O(1), O(1)
        if self.isEmpty():
            return None
        data = self.head.data
        #move head forward and sever the backward link
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def popBack(self): # Time, Space Complexities: O(1), O(1)
        if self.isEmpty():
            return None
        data = self.tail.data

        #Move tail backward and sever the forward link
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data

    def isEmpty(self): # Time, Space Complexities: O(1), O(1)
        return self.head is None