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
        if self.head is None:
            return None
        return self.head.data

    def back(self):
        if self.tail is None:
            return None
        return self.tail.data

    def pushBack(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        

    def pushFront(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def popFront(self):
        if self.head is None:
            return None
        
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return val
        

    def popBack(self):
        if self.tail is None:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return val

    def isEmpty(self):
        return self.head is None


if __name__ == "__main__":
    d = Deque()

    print(d.isEmpty())

    d.pushBack(1)
    d.pushBack(2)
    d.pushBack(3)

    print(d.front())
    print(d.back())

    d.pushFront(0)
    print(d.front())

    print(d.popFront())
    print(d.popBack())
    print(d.front())
    print(d.back())
    print(d.isEmpty())
