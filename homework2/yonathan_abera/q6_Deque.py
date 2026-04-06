class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
    def insertAtFront(head, val):
        new_node = Node(val)
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node
    
    def insertAtBack(head, tail, val):
        new_node = Node(val)
        if tail is None:
            return new_node, new_node
        tail.next = new_node
        new_node.prev = tail
        return head, new_node
    
    def insertAfter(head, val, loc):
        new_node = Node(val)
        new_node.next = loc.next
        new_node.prev = loc
        if loc.next:
            loc.next.prev = new_node
        loc.next = new_node
        return head
    
    def insertBefore(head, val, loc):
        new_node = Node(val)
        new_node.next = loc
        new_node.prev = loc.prev
        if loc.prev:
            loc.prev.next = new_node
        else:
            head = new_node
        loc.prev = new_node
        return head
    
    def deleteFront(head):
        if head is None:
            return None
        head = head.next
        if head:
            head.prev = None
        return head
    
    def deleteBack(head, tail):
        if tail is None:
            return None, None
        if tail.prev is None:
            return None, None
        tail = tail.prev
        tail.next = None
        return head, tail
    
    def deleteNode(head, loc):
        if loc.prev:
            loc.prev.next = loc.next
        else:
            head = loc.next
        if loc.next:
            loc.next.prev = loc.prev
        return head
    
    def length(head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def reverseIterative(head):
        curr = head
        new_head = None
        while curr:
            nxt = curr.next
            curr.next = curr.prev
            curr.prev = nxt
            new_head = curr
            curr = nxt
        return new_head
    
    def reverseRecursiveHelper(curr):
        if curr.next is None:
            curr.next = curr.prev
            curr.prev = None
            return curr
        nxt = curr.next
        new_head = Node.reverseRecursiveHelper(nxt)
        nxt.next = curr
        curr.prev = nxt
        curr.next = None
        return new_head
    
    def reverseRecursive(head):
        if head is None:
            return None
        return Node.reverseRecursiveHelper(head)
    
    def toList(head):
        result = []
        curr = head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
    
    def fromList(lst):
        head = None
        tail = None
        for val in lst:
            head, tail = Node.insertAtBack(head, tail, val)
        return head, tail

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def front(self):
        # O(1) time
        if self.head is None:
            return None
        return self.head.data
 
    def back(self):
        # O(1) time
        if self.tail is None:
            return None
        return self.tail.data
 
    def pushBack(self, x):
        # O(1) time
        self.head, self.tail = Node.insertAtBack(self.head, self.tail, x)
 
    def pushFront(self, x):
        # O(1) time
        self.head = Node.insertAtFront(self.head, x)
        if self.tail is None:
            self.tail = self.head
 
    def popFront(self):
        # O(1) time
        if self.head is None:
            return None
        val = self.head.data
        self.head = Node.deleteFront(self.head)
        if self.head is None:
            self.tail = None
        return val
 
    def popBack(self):
        # O(1) time
        if self.tail is None:
            return None
        val = self.tail.data
        self.head, self.tail = Node.deleteBack(self.head, self.tail)
        return val
 
    def isEmpty(self):
        # O(1) time
        return self.head is None