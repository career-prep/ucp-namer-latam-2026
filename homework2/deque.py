class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # back

    def front(self):                        
        if self.head is None:
            return -1
        return self.head.data

    def back(self):                         
        if self.tail is None:
            return -1
        return self.tail.data

    def pushBack(self, x):                  
        node = Node(x)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pushFront(self, x):                 
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def popFront(self):                     
        if self.head is None:
            return -1
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def popBack(self):                      
        if self.tail is None:
            return -1
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data

    def isEmpty(self):                      
        return self.head is None


# --- Tests ---
d = Deque()

# Test 1: isEmpty on new deque
print(d.isEmpty())        # True

# Test 2: pushBack and front/back
d.pushBack(10)
d.pushBack(20)
d.pushBack(30)
print(d.front())          # 10
print(d.back())           # 30

# Test 3: pushFront
d.pushFront(5)
print(d.front())          # 5
print(d.back())           # 30

# Test 4: popFront
print(d.popFront())       # 5
print(d.popFront())       # 10

# Test 5: popBack
print(d.popBack())        # 30
print(d.popBack())        # 20

# Test 6: isEmpty after all removed
print(d.isEmpty())        # True

# Test 7: popFront and popBack on empty
print(d.popFront())       # -1
print(d.popBack())        # -1

# Test 8: front and back on empty
print(d.front())          # -1
print(d.back())           # -1