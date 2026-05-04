"""40 minutes
Oluwatomi
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insertAtBack(self, data):
        if self.head is None:
            self.insertAtFront(data)
            return
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def insertAfter(self, data, location):
        new_node =  Node(data)
        new_node.prev = location
        new_node.next =  location.next
        if location.next:
            location.next.prev = new_node
        else:
            self.tail = new_node
        location.next = new_node
        
        return

    def insertBefore(self, data, location):
        if self.head == location:
            self.insertAtFront(data)
            return
        new_node = Node(data)
        new_node.next = location
        new_node.prev = location.prev
        location.prev.next = new_node
        location.prev = new_node


    def deleteFront(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        cur = self.head.next
        cur.prev = None
        self.head = cur
    def deleteBack(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        cur = self.tail.prev
        cur.next = None
        self.tail = cur
    
    def deleteNode(self, location):
        if location is None:
            return None
        if self.head == location:
            self.deleteFront()
            return
        if self.tail == location:
            self.deleteBack()
            return
        location.prev.next = location.next
        location.next.prev = location.prev


    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    def reverse_Iterative(self):
        if self.head is None:
            return
        cur = self.head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            cur.prev = temp
            prev = cur
            cur = temp
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data,  end=" <-> ")
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
