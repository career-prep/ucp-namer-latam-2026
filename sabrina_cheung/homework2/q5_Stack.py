'''
Time: 15 min
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insertAtFront(head, val):
    newhead = Node(val)
    newhead.next = head
    return newhead

def insertAtBack(head, val):
    if head == None:
        return Node(val)
    
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = Node(val)
    return head

def insertAfter(head, val, loc):
    newNode = Node(val)
    temp = loc.next
    loc.next = newNode
    newNode.next = temp
    
    return head

def insertBefore(head, val, loc):
    if head == None:
        return None
    
    cur = head
    prev = None
    while cur and cur is not loc:
        prev = cur
        cur = cur.next
    if cur is None:
        return head
    newNode = Node(val)
    prev.next = newNode
    newNode.next = cur
    return head

def deleteFront(head):
    if head == None:
        return None
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
        return head.next
    cur = head
    prev = None
    while cur and cur is not loc:
        prev = cur
        cur = cur.next
    if cur is None:
        return head
    prev.next = cur.next
    return head

def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def reverseIterative(head):
    if head == None:
        return None
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
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

class Stack:
    def __init__(self):
        self.head = None

    def top(self):
        if self.head == None:
            return None
        return self.head.data
    
    def push(self, x):
        if self.head == None:
            self.head = Node(x)
        else:
            temp = self.head
            self.head = Node(x)
            self.head.next = temp

    def pop(self):
        if self.head == None:
            return None
        val = self.head.data
        self.head = self.head.next
        return val
    
    def isEmpty(self):
        return self.head == None
    
    def printStack(self):
        stack_list = []
        cur = self.head
        while cur:
            stack_list.append(cur.data)
            cur = cur.next
        print(stack_list) 
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.printStack()

print(stack.top())
print(stack.pop())
print(stack.isEmpty())
print(stack.pop())
stack.printStack()