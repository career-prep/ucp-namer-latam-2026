"""40 minutes
Oluwatomi
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return 
    def insertAtBack(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    
    def insertAfter(self, data, location):
        new_node =  Node(data)
        new_node.next =  location.next
        location.next = new_node
        return

    def insertBefore(self, data, location):
        new_node = Node(data)
        if self.head == locaton:
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        while cur.next != location:
            cur = cur.next
        new_node.next = location
        cur.next = new_node

    def deleteFront(self):
        if self.head is None:
            return
        cur = self.head.next
        self.head = cur
    def deleteBack(self):
        if self.head is None:
            return
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next

        prev.next = None
    
    def deleteNode(self, location):
        if self.head == location:
            self.deleteFront()
            return
        cur = self.head
        prev = None
        while cur is not None and cur != location:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next

        return count
    def reverseIterative(self):
        if self.head is None:
            return
        cur = self.head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")




my_list = List()
my_list.insertAtFront(10)
my_list.insertAtFront(13)
my_list.print_list()
my_list.insertAtBack(15)
my_list.print_list()
print(my_list.length())
my_list.reverseIterative()
my_list.print_list()
