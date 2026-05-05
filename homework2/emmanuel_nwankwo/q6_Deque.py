class Node:
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class Deque:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # Time Complexity: O(1)
    def front(self):
        if self.head is None:
            return None
        return self.head.data

    # Time Complexity: O(1)
    def back(self):
        if self.tail is None:
            return None
        return self.tail.data

    # Time Complexity: O(1)
    def pushBack(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Time Complexity: O(1)
    def pushFront(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Time Complexity: O(1)
    def popFront(self):
        if self.head is None:
            return None
        head_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return head_data

    # Time Complexity: O(1)
    def popBack(self):
        if self.tail is None:
            return None
        tail_data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return tail_data

    # Time Complexity: O(1)
    def isEmpty(self):
        return self.head is None