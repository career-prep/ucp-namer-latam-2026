class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def front(self):
        # returns the first item in the deque. O(1) time.
        if self.head is None:
            return None
        return self.head.data

    def back(self):
        # returns the last item in the deque. O(1) time.
        if self.tail is None:
            return None
        return self.tail.data

    def pushBack(self, x):
        # adds x to the back of the deque. O(1) time.
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        if self.head is None:   
            self.head = new_node
        self.size += 1

    def pushFront(self, x):
        # adds x to the front of the deque. O(1) time.
        new_node = Node(x)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        if self.tail is None:  
            self.tail = new_node
        self.size += 1

    def popFront(self):
        # removes and returns the first item in the deque. O(1) time.
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:              
            self.tail = None
        self.size -= 1
        return val

    def popBack(self):
        # removes and returns the last item in the deque. O(1) time.
        if self.tail is None:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:              
            self.head = None
        self.size -= 1
        return val

    def isEmpty(self):
        # returns a boolean indicating whether the deque is empty. O(1) time.
        return self.head is None


if __name__ == "__main__":
    d = Deque()

    print(d.isEmpty())      # True

    d.pushBack(7)
    d.pushBack(12)
    d.pushFront(3)
    # deque: [3, 7, 12]

    print(d.front())        # 3
    print(d.back())         # 12

    print(d.popFront())     # 3
    print(d.popBack())      # 12
    # deque: [7]

    print(d.front())        # 7
    print(d.back())         # 7
    print(d.isEmpty())      # False

    print(d.popFront())     # 7
    print(d.isEmpty())      # True


    print(d.popFront())     # None
    print(d.popBack())      # None
