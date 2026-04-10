class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev =  None

class deque():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def returnFront(self):
        if not self.front:
            return "front is none"
        return self.front
    
    def returnBack(self):
        if not self.rear:
            return "back is none"
        return self.rear
    
    def pushBack(self, x):
        newNode = Node(x)

        if self.isEmpty():
            self.front = self.pushBack = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def pushFront(self, x):
        newNode = Node(x)

        if self.isEmpty():
            self.front = self.pushBack = newNode
        else:
            self.front.prev = newNode
            newNode.next = self.front
            self.front = newNode

    def popFront(self):
        if self.isEmpty():
            return "deque is empty"
        
        val = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        return val
    
    def popBack(self):
        if self.isEmpty():
            return "the deque is empty"
        
        val = self.rear.data
        self.back = self.back.prev

        if self.back is None:
            self.front = None
        else:
            self.back.next = None

        return val
