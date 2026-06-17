'''
Time: 20 mins
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head
    if head:
        head.prev = newhead
    return newhead

def insertAtBack(head, val):
    if head == None:
        return Node(val)
    
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = Node(val)
    cur.next.prev = cur
    return head

def insertAfter(head, val, loc):
    newNode = Node(val)
    temp = loc.next
    loc.next = newNode
    newNode.next = temp
    newNode.prev = loc

    if temp:
        temp.prev = newNode

    return head

def insertBefore(head, val, loc):
    new = Node(val)
    
    new.prev = loc.prev
    new.next = loc
    
    if loc.prev:
        loc.prev.next = new
    else:
        head = new
    
    loc.prev = new
    
    return head

def deleteFront(head):
    if head == None or head.next == None:
        return None

    head.next.prev = None
    return head.next

def deleteBack(head):
    if head == None or head.next == None:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head

def deleteNode(head, loc):
    if head == None:
        return None
    if head is loc:
        if head.next:
            head.prev = None
        return head.next
    
    if loc.next:
        loc.next.prev = loc.prev
    if loc.prev:
        loc.prev.next = loc.next
    return head

def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def reverseIterative(head):
    if head == None or head.next == None:
        return head
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        cur.prev = temp
        
        prev = cur
        cur = temp
    return prev

def reverseRecursive(head):
    if head == None:
        return None
    return recursiveSwap(head, None)

def recursiveSwap(cur, prev):
    if cur == None:
        return prev
    newNode = cur.next
    cur.next = prev

    return recursiveSwap(newNode, cur)

def print_list(head):
    linked_list = []
    while head:
        linked_list.append(head.data)
        head = head.next
    print(linked_list)

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if self.head == None:
            return None
        return self.head.data
    
    def back(self):
        if self.tail == None:
            return None
        return self.tail.data
    
    def pushBack(self, x):
        if self.tail == None:
            self.head = Node(x)
            self.tail = Node(x)
        else:
            self.tail.next = Node(x)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            

    def pushFront(self, x):
        newNode = Node(x)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = Node(x)
            self.head.next = temp
            temp.prev = self.head

    def popFront(self):
        if self.head == None:
            return None
        val = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return val
    
    def popBack(self):
        if self.tail == None:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return val
    
    def isEmpty(self):
        return self.head == None
    
    def printDeque(self):
        deque_list = []
        cur = self.head
        while cur:
            deque_list.append(cur.data)
            cur = cur.next
        print(deque_list) 
    
deque = Deque()
deque.pushFront(2)
deque.pushFront(1)
deque.pushBack(3)
deque.pushBack(4)
deque.printDeque()

print(deque.front())
print(deque.back())
print(deque.isEmpty())
print(deque.popFront())
print(deque.popBack())
deque.printDeque()